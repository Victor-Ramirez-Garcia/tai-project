from typing import List

class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)
        
        # Check missing types of characters
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing_types = (not has_lower) + (not has_upper) + (not has_digit)
        
        # Identify lengths of repeating character groups (length >= 3)
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
        if n < 6:
            # We need to insert (6 - n) characters. 
            # These insertions can also break up any repeats if managed properly, 
            # and can satisfy missing types. The dominating factor is max(6 - n, missing_types).
            return max(6 - n, missing_types)
            
        # Case 2: Length is between 6 and 20 (inclusive)
        elif n <= 20:
            # Each repeat group of size `k` requires `k // 3` replacements to break.
            # These replacements can also be used to satisfy missing types.
            replacements = sum(k // 3 for k in repeats)
            return max(replacements, missing_types)
            
        # Case 3: Length is greater than 20
        else:
            # We must delete (n - 20) characters.
            deletions = n - 20
            
            # Deletions can reduce the number of replacements needed to break repeat groups.
            # Priority 1: Groups where length % 3 == 0. Removing 1 char saves 1 replacement.
            # Priority 2: Groups where length % 3 == 1. Removing 2 chars saves 1 replacement.
            # Priority 3: Any other reduction (length % 3 == 2) saves 1 replacement per 3 deletions.
            
            # Priority 1: length % 3 == 0
            rem_deletions = deletions
            for i in range(len(repeats)):
                if rem_deletions > 0 and repeats[i] % 3 == 0:
                    repeats[i] -= 1
                    rem_deletions -= 1
                    
            # Priority 2: length % 3 == 1
            for i in range(len(repeats)):
                if rem_deletions >= 2 and repeats[i] % 3 == 1:
                    repeats[i] -= 2
                    rem_deletions -= 2
                    
            # Priority 3: length % 3 == 2 (or remaining length after above reductions)
            for i in range(len(repeats)):
                if rem_deletions > 0 and repeats[i] >= 3:
                    # Each 3 deletions reduces the remaining length and saves 1 replacement
                    possible_del = min(rem_deletions, repeats[i] - 2)
                    repeats[i] -= possible_del
                    rem_deletions -= possible_del
            
            # Calculate remaining replacements needed after all optimizations
            replacements = sum(k // 3 for k in repeats if k >= 3)
            
            # Total steps = deletions performed + max of remaining replacements or missing types
            return deletions + max(replacements, missing_types)