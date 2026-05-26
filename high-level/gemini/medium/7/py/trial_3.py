class Solution:

    def reverse(self, x: int) -> int:
        # Define the limits for a signed 32-bit integer
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        # Determine the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed