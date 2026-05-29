from typing import List
from collections import defaultdict

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        """
        Intuition:
        The problem asks us to find the maximum number of disjoint pairs of cards such that 
        each card in a pair contains the letter 'x' and the two cards differ in exactly 1 position.
        
        Since each card is a string of length 2, let's analyze the format of cards containing 'x':
        1. It can be "xx"
        2. It can be "ax" where a != x
        3. It can be "xa" where a != x
        
        Let's analyze compatibility (differing in exactly 1 position):
        - "xx" is compatible with "ax" (differs at index 0) and "xa" (differs at index 1).
        - "ax" is compatible with "bx" (differs at index 0) and "xx" (differs at index 0).
        - "xa" is compatible with "xb" (differs at index 1) and "xx" (differs at index 1).
        - Crucially, "ax" is NEVER compatible with "xb" because they differ in both positions 
          (index 0: a vs x, index 1: x vs a, assuming a != x and b != x).
          
        This means the cards form a bipartite graph structure! 
        - Left side: Cards of the form "ax" (where index 1 is 'x')
        - Right side: Cards of the form "xa" (where index 0 is 'x')
        - The card "xx" can connect to both sides.
        
        We can model this as finding the Maximum Bipartite Matching (or Max Flow). 
        However, since the graph structure is very constrained (only 26 letters), 
        we can count frequencies and use a greedy/matching approach or a simple Max Flow network.
        
        Let's count the exact occurrences of each card type:
        - count_xx: number of "xx" cards
        - left_counts[a]: number of "ax" cards (a != x)
        - right_counts[a]: number of "xa" cards (a != x)
        
        Self-matching:
        Can "ax" match with "bx"? Yes, they differ in exactly 1 position (index 0).
        Can "xa" match with "xb"? Yes, they differ in exactly 1 position (index 1).
        Can "xx" match with "xx"? No, they are identical (0 differences).
        
        Wait, if "ax" can match with "bx", this isn't purely bipartite between "ax" and "xa".
        Actually, ALL "ax" cards (for all a != x) are mutually compatible with each other!
        Because "ax" and "bx" differ only at index 0. 
        Similarly, ALL "xa" cards (for all a != x) are mutually compatible with each other.
        
        So the categories of cards are:
        - Group L: All cards matching the pattern ?x (excluding xx). Any two cards in Group L can match.
        - Group R: All cards matching the pattern x? (excluding xx). Any two cards in Group R can match.
        - Group C: Cards "xx". "xx" can match with any card in Group L, and any card in Group R.
        
        Let's verify:
        - Two cards from Group L: "ax" and "bx" -> differ at pos 0 -> Compatible.
        - Two cards from Group R: "xa" and "xb" -> differ at pos 1 -> Compatible.
        - One from L, one from R: "ax" and "xb" -> pos 0 differs (a vs x), pos 1 differs (x vs b) -> 2 differences. Not compatible.
        - "xx" and "ax" (from L) -> pos 0 differs -> Compatible.
        - "xx" and "xa" (from R) -> pos 1 differs -> Compatible.
        
        This simplifies things immensely!
        We can just count:
        - L = total number of "?x" cards where ? != x
        - R = total number of "x?" cards where ? != x
        - C = total number of "xx" cards
        
        Inside Group L, we can match cards internally. Each internal match takes 2 cards from L.
        Inside Group R, we can match cards internally. Each internal match takes 2 cards from R.
        We can also match a card from L with "xx", or a card from R with "xx".
        
        This can be solved by maximizing total pairs. This is equivalent to finding the maximum 
        matching in a graph where:
        - L items are fully connected to each other.
        - R items are fully connected to each other.
        - C items are connected to all L and all R items.
        
        Let's maximize pairs greedily or via a small state check.
        Total available cards: L, R, C.
        Since L items can pair with each other, any 2 items in L can form 1 point.
        Same for R.
        C can pair with L or R.
        
        Let's use a Max Flow / Min Cost approach or just test all possibilities for C since it's small, 
        but wait, we don't even need that. We can just use standard Max Flow (Edmonds-Karp or Dinic) 
        by representing each distinct card string as a node. Since there are at most 26*26 = 676 distinct 
        cards, a general maximum matching / max flow on the graph of actual card counts will be 
        extremely fast and robust against any misinterpretation of the greedy strategy.
        
        Let's build a network flow model:
        Each unique card string that contains 'x' is a node with a certain capacity (its count).
        Since it's an undirected matching problem on general graphs (or rather, a graph where we want 
        maximum edge-disjoint pairs), we can convert it into a Max Flow problem by splitting nodes 
        or using the Tutte-Berge formula, OR we can notice that the graph is actually very simple.
        
        Let's re-verify if L items can all pair with each other.
        "ax" and "ax": Can they pair? No, they are identical (0 differences).
        Ah! "ax" can only pair with "bx" where b != a.
        So Group L is a complete graph minus self-loops. This is a standard matching on a complete 
        graph of various frequencies.
        
        To be absolutely safe and optimal, we can treat this as a Maximum General Graph Matching 
        problem, but since the number of nodes is at most 51 ("ax" for 25 chars, "xa" for 25 chars, and "xx"),
        we can use Tutte's theorem or Edmonds' Blossom algorithm. But wait, it's even simpler:
        Let's look at the compatibility graph of unique card types:
        - "xx" is connected to all "ax" and all "xa".
        - "ax" is connected to all "bx" (b != a) and "xx".
        - "xa" is connected to all "xb" (b != a) and "xx".
        
        This is a graph with <= 51 vertices. Since we have multiple copies of each card, we can 
        just find the maximum matching.
        Alternatively, notice that:
        - All "ax" cards form a clique if they are distinct. Since we can't match identical cards, 
          the maximum number of pairs we can form purely within "ax" types is standard: 
          if one type has more than the sum of all others, it's limited; otherwise we can match 
          almost all of them.
        
        Let's formalize the matching within the "?x" group (Group L):
        We have counts for "ax", "bx", "cx", ...
        This is the classic "load balancing" or "discrete max pairs" problem.
        The max pairs we can form within Group L is min(total_L // 2, total_L - max_L), 
        where max_L is the maximum count of a single card type in L.
        
        Let's just use a backtracking search with memoization (or DP) if the states are small, 
        or a Max Flow if we can duplicate vertices. Since constraints on total cards aren't specified 
        but usually `len(cards) <= 10^5`, we can formulate this as a maximum flow or greedy.
        
        Let's use a Greedy Approach with a priority queue/sorted counts, or a formulation that solves 
        it directly.
        Actually, any card containing 'x' can be represented as a vertex. We want to find the max 
        pairs. We can greedily match the highest remaining compatible configurations.
        
        Let's build the explicit adjacency list of compatible *types*:
        There are at most 51 types of cards.
        Let's store the counts of each type.
        We can use a greedy strategy: always try to match the card type that has the highest count 
        with its compatible neighbor that has the highest count.
        To ensure accuracy, we can run a Max Flow on a transformed version, or since it's a 
        graph of 51 nodes, we can use a randomized greedy or Edmonds' Blossom if needed, 
        but let's see if it's bipartite.
        Is the graph bipartite?
        "ax" connects to "bx" -> odd cycles exist (e.g., "ax"-"bx"-"cx"-"ax"). So it's NOT bipartite.
        
        However, we can reduce the graph:
        All "ax" cards can match with "xx" or other "bx" cards.
        Let's use a greedy approach where we repeatedly take the two available compatible cards 
        that have the highest current remaining counts. This is a heuristic that works perfectly 
        for degree-monotone or highly symmetric graphs like cliques and bipartite graphs.
        
        Let's refine the greedy:
        In each step, find a pair of compatible card types (u, v) that are both available (count > 0) 
        such that we maximize some priority, or just use a standard state-based DP if the number of 
        card types is small? The number of card types is up to 51, but many will have count 0.
        
        Let's think if we can use Max Flow by splitting the graph.
        Any general graph matching can't be directly solved by Max Flow, but here the non-bipartite 
        parts are just two cliques (Group L and Group R) connected via a central node ("xx").
        - Group L: "ax" types. They form a complete graph where you can't match a type with itself.
        - Group R: "xa" types. They form a complete graph where you can't match a type with itself.
        - "xx": Connects to ALL nodes in Group L and Group R.
        
        Let's optimize the matching:
        1. "xx" can match with any node in L or R.
        2. Within L, we want to make as many pairs as possible.
        3. Within R, we want to make as many pairs as possible.
        
        If we match within L, each pair consumes 2 cards from L.
        If we match within R, each pair consumes 2 cards from R.
        If we match L with "xx", it consumes 1 from L and 1 from "xx".
        If we match R with "xx", it consumes 1 from R and 1 from "xx".
        
        Notice that matching within L is highly efficient because it saves "xx" for other uses.
        However, if there is a dominant element in L (say "ax" has 100 copies, and all other L have 0), 
        we cannot match "ax" within L. It MUST be matched with "xx".
        
        So for Group L, the number of leftover cards that CANNOT be matched internally is:
        `leftover_L = max(0, 2 * max_L - total_L)` if `total_L` is even, etc.
        More precisely, the maximum internal pairs in L is `internal_L = min(total_L // 2, total_L - max_L)`.
        The number of cards left unmatched internally in L is `rem_L = total_L - 2 * internal_L`.
        These `rem_L` cards are now "free" to be matched with anything else (including "xx" or each other 
        if the dominant element restriction is lifted, but by definition of `internal_L`, the remaining 
        cards are either all the same dominant card, or there's at most 1 card left if total_L was odd).
        
        Specifically:
        - If `max_L <= total_L // 2`: We can match almost all cards internally. `rem_L` is 0 (if total_L is even) or 1 (if odd). 
          If `rem_L == 1`, that 1 card can be any type, which can match with "xx".
        - If `max_L > total_L // 2`: We match all non-dominant cards with the dominant card. 
          The remaining cards are all of the dominant type ("ax"). Their count is `max_L - (total_L - max_L) = 2 * max_L - total_L`. 
          These remaining dominant cards CANNOT match with each other. They can ONLY match with "xx".
        
        This gives us the exact requirement for "xx":
        The dominant leftovers of L *must* match with "xx".
        The dominant leftovers of R *must* match with "xx".
        
        Let's calculate this precisely:
        For Group L:
        `total_L = sum(counts of "ax")`
        `max_L = max(counts of "ax")` (0 if empty)
        If `max_L > total_L - max_L`:
            `leftover_L_dominant = max_L - (total_L - max_L)`
            `internal_L_pairs = total_L - max_L`
        Else:
            `leftover_L_dominant = 0`
            `internal_L_pairs = total_L // 2`
        `unmatched_L_slack = total_L - 2 * internal_L_pairs - leftover_L_dominant` (This is either 0 or 1, representing an odd total_L where no single type dominates).
        
        Same logic applies to Group R to get `leftover_R_dominant`, `internal_R_pairs`, and `unmatched_R_slack`.
        
        Now, what can "xx" (count `C`) do?
        1. It MUST first help satisfy `leftover_L_dominant` and `leftover_R_dominant`.
           Why? Because those dominant leftover cards cannot match with anything else in their own group, and they can't match with the other group. They can ONLY match with "xx".
           So we greedily match `leftover_L_dominant` with `C`. Max matches = `min(leftover_L_dominant, C)`.
           Update `C` and `leftover_L_dominant`.
           Do the same for `leftover_R_dominant` and `C`.
           
        2. After satisfying the dominant leftovers, if we still have `leftover_L_dominant > 0`, these cards are completely stranded because `C` is exhausted.
        
        3. If `C > 0` after satisfying both dominant leftovers, what can `C` match with?
           It can match with any remaining slack or any cards currently paired internally in L or R!
           Wait, if `C` matches with an internally paired card in L (say "ax"-"bx"), we break that pair (losing 1 point), 
           but now "ax" pairs with "xx" (+1 point) and "bx" becomes free!
           If "bx" can then pair with something else (like a free card from R? No, L and R don't mix).
           Can "bx" pair with another free card from L? If there was one (slack), yes! That would increase the score.
           Actually, if `C > 0`, "xx" can just pair with any available card from L or R.
           If we have `unmatched_L_slack` (which is at most 1) or `unmatched_R_slack` (at most 1), `C` can pair with them directly.
           What if `C` is still greater than 0? It means we have extra "xx" cards, and all L and R cards are either fully matched or exhausted.
           Can we break an internal L-pair (2 cards) to match with 2 "xx" cards?
           Old: 1 pair (1 point). New: 2 pairs with "xx" (2 points). 
           Yes! Each internal pair in L uses 2 cards. If we have 2 "xx" cards, we can match both of those L cards with "xx" cards, gaining +1 net point.
           So each remaining "xx" can pair with ANY available single card from L or R.
           Since all dominant constraints are already resolved, any card in L or R is now flexible enough to be paired with "xx".
           
        Therefore, after resolving dominant leftovers, the remaining cards in L available for flexible pairing is `rem_flexible_L = total_L - cards_used_in_dominant_L`.
        Similarly for R: `rem_flexible_R = total_R - cards_used_in_dominant_R`.
        
        Let's double check this. Instead of a complex case analysis which might have edge cases, we can simulate the optimal matching by reducing it to a Max Flow problem or a simple Greedy on the counts.
        Since the number of distinct card types is at most 51, we can just use a Greedy approach with a priority queue/sorting or directly simulate the matching of pairs.
        
        Let's write a clean, robust Greedy simulation:
        We have a set of card types with their current counts.
        We want to find the max pairs.
        Since the graph is small, we can greedily pick the pair of compatible card types that maximizes the remaining options, or we can just use a Max Flow network!
        Wait, Max Flow works perfectly for Bipartite Matching, but our graph has cliques. Can we transform a clique matching into Max Flow?
        Yes, for a set of items where any two distinct types can match, the max pairs is `min(total // 2, total - max_count)`.
        
        Let's implement the precise mathematical formula based on the Group L, Group R, and Group C decomposition:
        
        Let's count:
        - `C`: count of "xx"
        - `L_counts`: dict of char -> count for "ax" (a != x)
        - `R_counts`: dict of char -> count for "xa" (a != x)
        
        `total_L = sum(L_counts.values())`
        `max_L = max(L_counts.values()) if L_counts else 0`
        `dom_L_char = max(L_counts, key=L_counts.get) if L_counts else ""`
        
        `total_R = sum(R_counts.values())`
        `max_R = max(R_counts.values()) if R_counts else 0`
        `dom_R_char = max(R_counts, key=R_counts.get) if R_counts else ""`
        
        Let's determine how many dominant cards in L are completely forced to match outside of L:
        `forced_L = max(0, max_L - (total_L - max_L))`
        `internal_L = (total_L - forced_L) // 2`
        `slack_L = (total_L - forced_L) % 2`
        
        Same for R:
        `forced_R = max(0, max_R - (total_R - max_R))`
        `internal_R = (total_R - forced_R) // 2`
        `slack_R = (total_R - forced_R) % 2`
        
        Now, the `forced_L` cards can ONLY match with "xx".
        The `forced_R` cards can ONLY match with "xx".
        
        Let's match them with `C`:
        `match_forced_L = min(forced_L, C)`
        `C -= match_forced_L`
        `forced_L -= match_forced_L`
        
        `match_forced_R = min(forced_R, C)`
        `C -= match_forced_R`
        `forced_R -= match_forced_R`
        
        Points so far = `internal_L + internal_R + match_forced_L + match_forced_R`
        
        If `C > 0`:
        Now all remaining cards in L (which are currently formed into `internal_L` pairs and `slack_L`) and R (formed into `internal_R` pairs and `slack_R`) are fully compatible with "xx".
        Crucially, any card in L or R can pair with "xx". 
        The number of available cards in L and R that can be paired with the remaining `C` cards is:
        `available_L = 2 * internal_L + slack_L`
        `available_R = 2 * internal_R + slack_R`
        `total_available = available_L + available_R`
        
        Each "xx" card can take 1 available card to form 1 point. But wait! If it takes a card that was already in an internal pair, we dissolve that internal pair (-1 point) and make a new pair with "xx" (+1 point), resulting in 0 net change in points... WAIT.
        Ah! If we dissolve an internal pair of 2 cards, we have TWO cards available. If we have 2 "xx" cards, we can match both, getting 2 points (net +1).
        So, effectively, each "xx" card can match with any available card. The total number of unique pairings we can achieve from the pool of `total_available` cards and `C` central cards, plus internal matchings, is simply:
        We have a pool of `total_available` cards and `C` cards. Since `C` can match with anything in the pool, and the pool items can match among themselves (with the condition that no single type dominates anymore, which is true because the dominant ones were subtracted), the maximum number of pairs we can form from the remaining components is:
        `(total_available + C) // 2` capped by the total number of elements? No, `C` can only match with pool elements, it cannot match with itself.
        So it's a bipartite-like matching between `C` and the pool, plus internal matching within the pool.
        Since any element in the pool can match with `C`, and pool elements can match with each other, the maximum pairs is simply `min((total_available + C) // 2, total_available)`.
        Let's verify: if `C >= total_available`, we can match all `total_available` cards with `C` cards, getting `total_available` pairs.
        If `C < total_available`, we can match `C` cards with `C` pool cards, leaving `total_available - C` cards in the pool, which can be paired internally to get `(total_available - C) // 2` pairs. Total pairs = `C + (total_available - C) // 2 = (total_available + C) // 2`.
        
        This is incredibly elegant and perfectly accounts for breaking internal pairs to match with "xx"!
        
        Let's double check if there's any restriction. Are we sure that after removing `forced_L`, the remaining `available_L` cards can still be perfectly paired internally or with `C` without violating the dominant condition?
        Yes, because by definition, after removing `forced_L` dominant cards, the maximum count of any single type in the remaining L pool is exactly equal to the sum of the rest of the types in the remaining L pool (or less). Thus, no single type dominates the remaining pool, meaning they can be fully paired dynamically.
        
        Let's double check with an example:
        cards = ["ax", "bx", "xx", "xx"], x = "x"
        L: "ax": 1, "bx": 1 -> total_L = 2, max_L = 1.
        forced_L = max(0, 1 - 1) = 0.
        internal_L = 2 // 2 = 1. slack_L = 0.
        C = 2.
        Points so far = 1 (from internal_L) + 0 + 0 = 1.
        C remaining = 2.
        available_L = 2. available_R = 0. total_available = 2.
        Since C = 2, min((2+2)//2, 2) = 2.
        Total points = 0 (reset old internal) + 2 = 2.
        Pairs: ("ax", "xx") and ("bx", "xx"). Total points = 2. Correct!
        
        Another example:
        cards = ["ax", "ax", "xx"], x = "x"
        L: "ax": 2 -> total_L = 2, max_L = 2.
        forced_L = max(0, 2 - 0) = 2.
        internal_L = 0, slack_L = 0.
        C = 1.
        match_forced_L = min(2, 1) = 1.
        C becomes 0. forced_L becomes 1.
        Points so far = 1.
        Remaining C = 0.
        Total points = 1. Correct (pair "ax" and "xx", one "ax" left over).
        
        Complexity:
        Time: O(N) to populate the frequency counts, where N is the number of cards.
        Space: O(1) as the dictionary sizes are bounded by the alphabet size (26).
        """
        
        # Count frequencies of each card type containing 'x'
        c_count = 0
        l_counts = defaultdict(int)
        r_counts = defaultdict(int)
        
        for card in cards:
            if x not in card:
                continue
            if card == x + x:
                c_count += 1
            elif card[1] == x:
                l_counts[card[0]] += 1
            elif card[0] == x:
                r_counts[card[1]] += 1
                
        # Analyze Group L (?x)
        total_l = sum(l_counts.values())
        max_l = max(l_counts.values()) if l_counts else 0
        forced_l = max(0, max_l - (total_l - max_l))
        internal_l = (total_l - forced_l) // 2
        slack_l = (total_l - forced_l) % 2
        
        # Analyze Group R (x?)
        total_r = sum(r_counts.values())
        max_r = max(r_counts.values()) if r_counts else 0
        forced_r = max(0, max_r - (total_r - max_r))
        internal_r = (total_r - forced_r) // 2
        slack_r = (total_r - forced_r) % 2
        
        # Greedily match forced dominant cards with 'xx'
        match_forced_l = min(forced_l, c_count)
        c_count -= match_forced_l
        
        match_forced_r = min(forced_r, c_count)
        c_count -= match_forced_r
        
        # Base points from forced matches
        points = match_forced_l + match_forced_r
        
        # Remaining flexible cards from L and R pools
        available_l = 2 * internal_l + slack_l
        available_r = 2 * internal_r + slack_r
        total_available = available_l + available_r
        
        # Combine the remaining flexible pool with the remaining 'xx' cards
        points += min((total_available + c_count) // 2, total_available)
        
        return points