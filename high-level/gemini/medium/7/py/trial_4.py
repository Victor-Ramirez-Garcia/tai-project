class Solution:

    def reverse(self, x: int) -> int:
        # Define the limits for a signed 32-bit integer
        INT_MIN, INT_MAX = -(2**31), 2**31 - 1

        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x != 0:
            pop = x % 10
            x //= 10

            # Check for overflow before updating res
            if res > (INT_MAX - pop) // 10:
                return 0

            res = res * 10 + pop

        return sign * res