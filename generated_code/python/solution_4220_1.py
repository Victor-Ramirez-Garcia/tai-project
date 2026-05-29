from typing import List

class Solution:
    def minOperations(self, s: str) -> int:
        # If the string is already sorted, 0 operations are required.
        if s == "".join(sorted(s)):
            return 0
        
        # An operation allows sorting any substring that is NOT the entire string.
        # This means we can sort any prefix of length up to n-1, or any suffix of length up to n-1.
        # 
        # Case 1: Can we do it in 1 operation?
        # We can do it in 1 operation if the character that is supposed to be at the 
        # first position is already at the first position, OR the character that is 
        # supposed to be at the last position is already at the last position.
        # - If s[0] == min_char, we can sort the suffix s[1:] (length n-1) to sort the whole string.
        # - If s[-1] == max_char, we can sort the prefix s[:n-1] (length n-1) to sort the whole string.
        
        sorted_s = sorted(s)
        min_char = sorted_s[0]
        max_char = sorted_s[-1]
        
        if s[0] == min_char or s[-1] == max_char:
            return 1
            
        # Case 2: Can we do it in 2 operations?
        # If the above isn't true, we can always do it in 2 operations EXCEPT for one specific case.
        # Operation 1: Sort the prefix s[:n-1]. This guarantees that the largest character (max_char)
        # moves to index n-2 (since the very last character s[-1] is left untouched).
        # Operation 2: Now that max_char is at index n-2, we can sort the suffix s[1:]. This will
        # correctly move max_char to the very end (index n-1) and sort the rest of the string.
        # 
        # However, this 2-operation strategy fails if the absolute maximum character is at the 
        # very beginning (s[0] == max_char) AND the absolute minimum character is at the 
        # very end (s[-1] == min_char). 
        # If s[0] == max_char and s[-1] == min_char, sorting s[:n-1] will move min_char somewhere 
        # inside, but max_char will move to index n-2. Then sorting s[1:] will move max_char to index n-1, 
        # but the min_char that was at index n-1 originally is now mixed into the middle and cannot 
        # reach index 0 because index 0 is excluded from the second operation.
        #
        # Case 3: When s[0] == max_char and s[-1] == min_char, it takes 3 operations.
        # Op 1: Sort any middle substring to move things around, or just sort s[1:] to move min_char 
        # away from the end. 
        # Op 2: Sort s[:n-1] to bring min_char to the front.
        # Op 3: Sort s[1:] to finish sorting the rest.
        if s[0] == max_char and s[-1] == min_char:
            return 3
            
        return 2