from typing import List

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        # Count missing character types (lowercase, uppercase, digit)
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = (1 if not has_lower else 0) + (1 if not has_upper else 0) + (1 if not has_digit else 0)
        
        n = len(password)
        
        # Find all repeating blocks of length >= 3
        # We store the length of each repeating block
        repeats = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            length = j - i
            if length >= 3:
                repeats.append(length)
            i = j
            
        # Case 1: Length is less than 6
        # We only need insertions. Each insertion can also fix a missing type
        # and potentially break a repeating block. Max required is max(6 - n, missing_types).
        if n < 6:
            return max(6 - n, missing_types)
            
        # Case 2: Length is between 6 and 20 (inclusive)
        # We can use replacements to fix missing types and break repeating blocks.
        # Each replacement reduces a repeating block length by 3 (e.g., len 3->0, len 5->2).
        elif n <= 20:
            replace_needed = sum(length // 3 for length in repeats)
            return max(replace_needed, missing_types)
            
        # Case 3: Length is greater than 20
        # We must delete (n - 20) characters. We should prioritize deletions that 
        # reduce the number of replacements needed to break up repeating blocks.
        # A block of length L requires L // 3 replacements.
        # - Deleting 1 char from a block where L % 3 == 0 reduces replacements by 1.
        # - Deleting 2 chars from a block where L % 3 == 1 reduces replacements by 1.
        # - Deleting 3 chars from a block where L % 3 == 2 reduces replacements by 1.
        else:
            deletions = n - 20
            left_deletions = deletions
            
            # Phase 1: Subtraction from groups where length % 3 == 0
            # Each deletion here saves 1 replacement.
            for i in range(len(repeats)):
                if left_deletions > 0 and repeats[i] % 3 == 0:
                    repeats[i] -= 1
                    left_deletions -= 1
                    
            # Phase 2: Subtraction from groups where length % 3 == 1
            # Each pair of deletions here saves 1 replacement.
            for i in range(len(repeats)):
                if left_deletions >= 2 and repeats[i] % 3 == 1:
                    repeats[i] -= 2
                    left_deletions -= 2
                    
            # Phase 3: Subtraction from any remaining groups
            # Each remaining group needs 3 deletions to save 1 replacement.
            for i in range(len(repeats)):
                if left_deletions > 0 and repeats[i] >= 3:
                    # Calculate how many replacements we can eliminate
                    possible_del = repeats[i] - 2
                    actual_del = min(left_deletions, possible_del)
                    repeats[i] -= actual_del
                    left_deletions -= actual_del
                    
            # Total replacements needed after optimal deletions
            replace_needed = sum(length // 3 for length in repeats)
            
            return deletions + max(replace_needed, missing_types)