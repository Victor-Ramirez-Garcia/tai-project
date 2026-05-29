from typing import List, Dict

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        """
        Calculates the maximum points by finding the maximum matching in a graph
        where edges connect "compatible" cards that both contain the letter 'x'.
        Two cards are compatible if they differ in exactly 1 position.
        
        Since cards are length 2, they contain 'x' if they are of the form:
        1. "xx"
        2. "x?" (where ? is any char)
        3. "?x" (where ? is any char)
        
        Compatibility rules:
        - "xx" differs by 1 position from any "x?" or "?x" (where ? != 'x').
        - "x?" and "x!" differ by 1 position if ? != !.
        - "?x" and "!x" differ by 1 position if ? != !.
        - "x?" and "!x" differ by 2 positions (unless ?=='x' or !=='x'), so they are NOT compatible.
        
        This structure naturally forms a Bipartite Graph:
        - Set A: Cards of the form "x?" (where 'x' is at index 0)
        - Set B: Cards of the form "?x" (where 'x' is at index 1)
        - Note: "xx" belongs to both conceptual styles, but it connects to all "x?" and "?x".
        Actually, we can model this as a Maximum Cardinality Matching problem on a general graph,
        or observe the components. Since N is typically small in such card games or can be solved
        using a standard Maximum Bipartite Matching (or Blossom algorithm if general).
        Wait, does "x?" connect to "x!"? Yes, they differ in exactly 1 position (the second one).
        So "x?" cards form a clique among themselves! "?x" cards form a clique among themselves!
        And "xx" connects to all "x?" and all "?x".
        
        Let's count the frequencies of each unique card containing 'x'.
        Let c_xx be count of "xx".
        Let c_x[x] be count of "xx" (handled separately).
        For any char c != x:
          Let count of "xc" be count_left[c]
          Let count of "cx" be count_right[c]
          
        Connections:
        - "xc" is compatible with "xd" for all d. (Clique of left cards)
        - "cx" is compatible with "dx" for all d. (Clique of right cards)
        - "xx" is compatible with all "xc" and all "cx".
        - "xc" is NEVER compatible with "dy" (where c, y != x).
        
        So the graph consists of:
        - A set of "left" cards ("xc"). They are all mutually compatible.
        - A set of "right" cards ("cx"). They are all mutually compatible.
        - "xx" cards, which are compatible with EVERY left card and EVERY right card.
        Note: "xx" cards are NOT compatible with other "xx" cards (difference is 0 positions).
        "xc" is NOT compatible with "xc" (difference is 0).
        
        Thus, any two distinct "xc" and "xd" can match. Any two distinct "cx" and "dx" can match.
        "xx" can match with any "xc" or any "cx".
        
        This is a small general graph matching problem, or we can solve it greedily/combinatorially.
        Total valid cards available:
        - left_cards: list of all "xc" cards (including multiple copies, but we can only match distinct strings).
          Wait! "xc" and "xc" are identical, difference is 0, so they CANNOT match each other.
          So we can only match "xc" with "xd" where c != d.
        
        Let's formalize the matching rules between individual card instances:
        Instance i and Instance j can match if they are distinct strings and both contain 'x' and differ by 1 char.
        - "xx" matches "xc" (c != x)
        - "xx" matches "cx" (c != x)
        - "xc" matches "xd" (c != d, both != x)
        - "cx" matches "dx" (c != d, both != x)
        
        Since we want maximum matching, we can use the Blossom algorithm or Max Flow if it's bipartite. 
        Is it bipartite? 
        "xa" - "xb" - "xc" forms a triangle? Yes, "xa" and "xb" differ by 1, "xb" and "xc" by 1, "xa" and "xc" by 1.
        So it's NOT bipartite. We need a General Graph Maximum Matching (Blossom Algorithm), 
        or since the constraints on alphabet size are small (26), we can use a backtracking/DP search 
        or a standard Blossom implementation.
        Given it's LeetCode, constraints on `cards.length` are usually up to 10^4, but the number of *unique* cards is at most 52 (26 of "xc" and 26 of "cx").
        Let's count the number of each card type. 
        We have:
        - count["xx"]
        - count["xc"] for c in 'a'..'z' (c != 'x')
        - count["cx"] for c in 'a'..'z' (c != 'x')
        
        Since we want to maximize pairs:
        Any matching reduces the counts. We can use a backtracking search with memoization (DP) 
        on the counts of the 51 types of cards? No, 51 counts is too large for state space if counts are large.
        But notice that all "xc" types are symmetric except for their available counts.
        Actually, we can just find the maximum matching using a standard Edmonds' Blossom algorithm 
        on the explicit graph of card instances if N is small, OR build the graph on instances.
        If N is up to 10^5, an instance graph is too big. But most cards are duplicates.
        Duplicates of "xc" cannot match with each other. They can only match with "xd" (d != c) or "xx" or "cx".
        Wait, "xc" does NOT match with "cx"! "xc" and "cx" differ in 2 positions if c != x.
        
        Let's implement a general Max Matching via standard BFS-based Blossom Algorithm.
        To handle large N, we can optimize: duplicate cards of the same type can only match with cards of *other* allowed types.
        Maximum unique types = 51.
        If we create a graph where each type has a certain capacity?
        Alternatively, we can greedily match duplicates? 
        No, let's look at the maximum number of useful instances. For a single type, say "xa", it can at most match with all other available nodes.
        We can bound the count of each type to at most 51 (since there are at most 51 other types, a type can't match more than the total number of other vertices).
        So we can cap the count of each card type to `min(count, 51)`.
        Thus, the total number of vertices in our instance graph will be at most 51 * 51 ≈ 2600.
        An $O(V^3)$ or $O(V \cdot E)$ Blossom algorithm will easily run within time limits for $V \le 2600$.
        """
        
        # 1. Count frequencies of valid cards containing 'x'
        counts: Dict[str, int] = {}
        for card in cards:
            if 'x' in card:
                counts[card] = counts.get(card, 0) + 1
                
        # 2. Filter and cap counts to avoid graph explosion
        # A single card type can match at most once with any other single node.
        # Max distinct other card types is 51. So cap at 51.
        capped_cards = []
        for card, qty in counts.items():
            limit = min(qty, 52)
            for _ in range(limit):
                capped_cards.append(card)
                
        num_nodes = len(capped_cards)
        if num_nodes < 2:
            return 0
            
        # 3. Build adjacency list for the Blossom algorithm
        adj = [[] for _ in range(num_nodes)]
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                c1, c2 = capped_cards[i], capped_cards[j]
                # They must be compatible: differ in exactly 1 position
                diff = 0
                if c1[0] != c2[0]: diff += 1
                if c1[1] != c2[1]: diff += 1
                if diff == 1:
                    adj[i].append(j)
                    adj[j].append(i)
                    
        # 4. Edmonds' Blossom Algorithm for Maximum Cardinality Matching
        match = [-1] * num_nodes
        parent = [-1] * num_nodes
        base = list(range(num_nodes))
        used = [False] * num_nodes
        blossom = [False] * num_nodes
        
        def lca(u: int, v: int) -> int:
            path_b = [False] * num_nodes
            while True:
                u = base[u]
                path_b[u] = True
                if match[u] == -1:
                    break
                u = parent[match[u]]
            while True:
                v = base[v]
                if path_b[v]:
                    return v
                v = parent[match[v]]

        def mark_blossom(u: int, v: int, b: int) -> None:
            while base[u] != b:
                v = match[u]
                blossom[base[u]] = blossom[base[v]] = True
                parent[u] = v
                u = parent[v]

        def augment(start: int) -> bool:
            nonlocal parent, base, used, blossom
            used = [False] * num_nodes
            parent = [-1] * num_nodes
            base = list(range(num_nodes))
            
            queue = [start]
            used[start] = True
            head = 0
            
            while head < len(queue):
                u = queue[head]
                head += 1
                
                for v in adj[u]:
                    if base[u] == base[v] or match[u] == v:
                        continue
                    if v == start or (match[v] != -1 and parent[match[v]] != -1):
                        # Blossom found
                        b = lca(u, v)
                        blossom = [False] * num_nodes
                        mark_blossom(u, v, b)
                        mark_blossom(v, u, b)
                        for i in range(num_nodes):
                            if blossom[base[i]]:
                                base[i] = b
                                if not used[i]:
                                    used[i] = True
                                    queue.append(i)
                    elif parent[v] == -1:
                        parent[v] = u
                        if match[v] == -1:
                            # Augmenting path found, remap matches
                            curr = v
                            while curr != -1:
                                p = parent[curr]
                                nxt = match[p]
                                match[curr] = p
                                match[p] = curr
                                curr = nxt
                            return True
                        used[match[v]] = True
                        queue.append(match[v])
            return False

        # Find maximum matching
        max_matching = 0
        for i in range(num_nodes):
            if match[i] == -1:
                if augment(i):
                    max_matching += 1
                    
        return max_matching