class Solution:

    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer limits
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x != 0:
            #