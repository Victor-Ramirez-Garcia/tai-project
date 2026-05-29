class Solution:
    def hasSameDigits(self, s: str) -> bool:
        # Since the problem constraints for Version I are typically small (3 <= s.length <= 100),
        # an iterative O(N^2) simulation approach is optimal and clean. 
        # For each pass, we compute the adjacent sums modulo 10.
        digits = [int(c) for c in s]
        
        while len(digits) > 2:
            new_digits = []
            for i in range(len(digits) - 1):
                new_digits.append((digits[i] + digits[i + 1]) % 10)
            digits = new_digits
            
        return digits[0] == digits[1]