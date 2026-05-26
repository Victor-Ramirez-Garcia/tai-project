class Solution:
    def reverse(self, x: int) -> int:
        # Define 32-bit signed integer limits
        MIN_INT, MAX_INT = -2147483648, 2147483647
        
        res = 0
        # Determine the sign and work with absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            # Extract the last digit
            pop = x % 10
            x //= 10
            
            # Check for overflow before updating res
            # If res > MAX_INT // 10, the next step will definitely overflow
            # If res == MAX_INT // 10, we check if the digit 'pop' exceeds the last digit of MAX_INT (7)
            if res > MAX_INT // 10 or (res == MAX_INT // 10 and pop > 7):
                return 0
                
            res = (res * 10) + pop
            
        return res * sign