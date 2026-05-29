from typing import List
from collections import defaultdict

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        # Filter cards to only those that contain the character 'x'
        valid_cards = [card for card in cards if x in card]
        if not valid_cards:
            return 0
            
        # Group cards by their frequency of characters to quickly find potential matches.
        # Since each card has exactly 2 lowercase letters, they can either be:
        # 1. Double letters (e.g., "aa", "bb")
        # 2. Distinct letters (e.g., "ab", "ba") - Note: order matters for "differ in exactly 1 position".
        # Two cards of length 2 differ in exactly 1 position if they share exactly 1 character 
        # at the exact same index. For example, "ax" and "bx" differ at index 0.
        # This problem can be modeled as finding the maximum matching in a graph where 
        # nodes are valid cards and edges connect compatible cards.
        # Since the graph is small or can be split into independent components, we can use 
        # a standard maximum matching approach or greedy/counting strategies based on card types.
        
        # Let's count the occurrences of each unique 2-letter string
        counts = defaultdict(int)
        for card in valid_cards:
            counts[card] += 1
            
        # Build an adjacency list for the matching graph. 
        # Vertices will be the unique cards.
        unique_cards = list(counts.keys())
        n = len(unique_cards)
        
        adj = defaultdict(list)
        for i in range(n):
            u = unique_cards[i]
            for j in range(i + 1, n):
                v = unique_cards[j]
                # Check if u and v differ in exactly 1 position
                if (u[0] == v[0] and u[1] != v[1]) or (u[0] != v[0] and u[1] == v[1]):
                    adj[u].append(v)
                    adj[v].append(u)
                    
        # Since we can have multiple copies of the same card, identical cards cannot be 
        # compatible with each other because they differ in 0 positions.
        # Thus, any matching must happen between different card types.
        # We can expand the graph to include all individual cards, or use a flow/matching 
        # algorithm that accounts for capacities (demands).
        # Given it's a general graph matching problem with capacities, we can unroll the 
        # counts into individual nodes if the total number of cards is reasonably small, 
        # or use Edmonds' Blossom algorithm / Max Flow if it forms a bipartite graph.
        
        # Let's check if the graph is bipartite. Every valid card contains 'x'.
        # A card can have 'x' at index 0, index 1, or both ("xx").
        # Case 1: "xx" -> differs from "ax" at index 0, and from "xa" at index 1.
        # Case 2: "ax" (x at index 1) -> can only match with "bx" (x at index 1) or "xx".
        # Notice that "ax" and "xb" differ in BOTH positions (index 0: a vs x, index 1: x vs b).
        # So a card with x at index 1 ("_x") CANNOT match with a card with x at index 0 ("x_"),
        # UNLESS one of them is "xx".
        # This implies the graph components are:
        # Group A: Cards of form "cx" where c != x
        # Group B: Cards of form "xc" where c != x
        # Node "xx": Connects to all "cx" (differ at index 0) and all "xc" (differ at index 1).
        # There are NO edges between Group A and Group B directly.
        # Edges only exist:
        # - Within Group A: "ax" and "bx" differ at index 0 (exactly 1 position). So Group A is a clique!
        # - Within Group B: "xa" and "xb" differ at index 1 (exactly 1 position). So Group B is a clique!
        # - Between "xx" and Group A, and between "xx" and Group B.
        
        # Since Group A forms a clique and Group B forms a clique, we can optimize the matching.
        # Let's count total cards in Group A, Group B, and "xx".
        count_xx = counts["xx"]
        
        group_A_total = 0
        for card, qty in counts.items():
            if card != "xx" and card[1] == x:
                group_A_total += qty
                
        group_B_total = 0
        for card, qty in counts.items():
            if card != "xx" and card[0] == x:
                group_B_total += qty
                
        # We want to maximize pairs. 
        # Inside Group A, any two cards are compatible. So we can pair them up greedily.
        # Inside Group B, any two cards are compatible. So we can pair them up greedily.
        # "xx" can pair with ANY card in Group A or Group B.
        # This can be solved by iterating over how many "xx" cards pair with Group A vs Group B.
        
        max_points = 0
        # Iterate over all possible number of "xx" cards assigned to pair with Group A
        for xx_to_A in range(count_xx + 1):
            xx_to_B = count_xx - xx_to_A
            
            # Remaining single cards in Group A after pairing with xx_to_A
            # Each "xx" takes 1 card from Group A
            rem_A = max(0, group_A_total - xx_to_A)
            pairs_from_A_and_xx = min(group_A_total, xx_to_A) + (rem_A // 2)
            
            # Remaining single cards in Group B after pairing with xx_to_B
            rem_B = max(0, group_B_total - xx_to_B)
            pairs_from_B_and_xx = min(group_B_total, xx_to_B) + (rem_B // 2)
            
            total_pairs = pairs_from_A_and_xx + pairs_from_B_and_xx
            if total_pairs > max_points:
                max_points = total_pairs
                
        return max_points