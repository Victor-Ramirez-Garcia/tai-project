from typing import List

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        # 1. Count missing character types (lowercase, uppercase, digit)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = (1 if not has_lower else 0) + (1 if not has_upper else 0) + (1 if not has_digit else 0)
        
        # 2. Find all repeating sequences of length >= 3
        # We store the lengths of these repeating groups
        repeating_groups = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                repeating_groups.append(length)
            i = j
            
        # --- Case 1: Short password (len < 6) ---
        # We only need to insert characters. Each insertion can also break a repeating triplet.
        # Total steps is the max of required insertions to reach length 6 and missing types.
        if n < 6:
            return max(6 - n, missing_types)
            
        # --- Case 2: Standard length (6 <= len <= 20) ---
        # We can fix triplets purely by replacements. 
        # Each triplet of length L needs L // 3 replacements.
        elif n <= 20:
            replacements = sum(length // 3 for length in repeating_groups)
            return max(replacements, missing_types)
            
        # --- Case 3: Overly long password (len > 20) ---
        # We MUST delete exactly (n - 20) characters.
        # Strategy: Use deletions effectively to reduce the total number of required replacements.
        # A repeating group of length L requires L // 3 replacements.
        # - If L % 3 == 0, 1 deletion reduces replacements by 1 (e.g., length 3 -> 2, replacements 1 -> 0).
        # - If L % 3 == 1, 2 deletions reduce replacements by 1 (e.g., length 4 -> 2, replacements 1 -> 0).
        # - If L % 3 == 2, 3 deletions reduce replacements by 1 (e.g., length 5 -> 2, replacements 1 -> 0).
        else:
            deletions_needed = n - 20
            
            # Priority 1: Groups with length % 3 == 0 (costs 1 deletion to save 1 replacement)
            for i in range(len(repeating_groups)):
                if deletions_needed <= 0:
                    break
                if repeating_groups[i] % 3 == 0:
                    repeating_groups[i] -= 1
                    deletions_needed -= 1
                    
            # Priority 2: Groups with length % 3 == 1 (costs 2 deletions to save 1 replacement)
            for i in range(len(repeating_groups)):
                if deletions_needed <= 0:
                    break
                if repeating_groups[i] % 3 == 1:
                    # We can use up to 2 deletions for this group
                    rem = min(deletions_needed, 2)
                    repeating_groups[i] -= rem
                    deletions_needed -= rem
                    
            # Priority 3: Groups with length % 3 == 2 (costs 3 deletions to save 1 replacement)
            for i in range(len(repeating_groups)):
                if deletions_needed <= 0:
                    break
                if repeating_groups[i] >= 3:
                    # Each 3 deletions reduces length and saves 1 replacement
                    # We look at how many replacements are left that can be removed by 3 deletions
                    possible_3s_to_remove = repeating_groups[i] // 3
                    rem = min(deletions_needed, possible_3s_to_remove * 3)
                    repeating_groups[i] -= rem
                    deletions_needed -= rem
            
            # Calculate final replacements needed after optimization
            replacements = sum(length // 3 for length in repeating_groups if length >= 3)
            
            # Total steps = deletions made + max of remaining replacements or missing types
            return (n - 20) + max(replacements, missing_types)