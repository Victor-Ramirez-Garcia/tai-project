#include <gtest/gtest.h>
#include <string>
#include "solution_proxy.h"

// Test case for the provided example in the problem statement
TEST(LongestBalancedTest, ExampleCase) {
    Solution sol;
    // Example: "100001" -> Swap to "101000" -> Substring "1010" has length 4
    EXPECT_EQ(sol.longestBalanced("100001"), 4);
}

// Test cases for minimum input constraints (Single character strings)
TEST(LongestBalancedTest, MinimumLengthConstraints) {
    Solution sol;
    EXPECT_EQ(sol.longestBalanced("0"), 0);
    EXPECT_EQ(sol.longestBalanced("1"), 0);
}

// Test cases for strings that are already balanced or easily balanced
TEST(LongestBalancedTest, SmallBalancedStrings) {
    Solution sol;
    EXPECT_EQ(sol.longestBalanced("01"), 2);
    EXPECT_EQ(sol.longestBalanced("10"), 2);
    EXPECT_EQ(sol.longestBalanced("0011"), 4);
}

// Test cases where no '0's or no '1's exist (impossible to have a balanced substring > 0)
TEST(LongestBalancedTest, AllIdenticalCharacters) {
    Solution sol;
    EXPECT_EQ(sol.longestBalanced("00000"), 0);
    EXPECT_EQ(sol.longestBalanced("11111"), 0);
}

// Test cases requiring exactly one swap to optimize the balanced substring length
TEST(LongestBalancedTest, OneSwapOptimization) {
    Solution sol;
    // Swap first '1' with third '0': "111000" -> "011100" -> Substring "011100" is balanced (length 6)
    EXPECT_EQ(sol.longestBalanced("111000"), 6);
    // Swap to bring trapped characters together
    EXPECT_EQ(sol.longestBalanced("000111"), 6);
    EXPECT_EQ(sol.longestBalanced("101010"), 6);
}

// Test cases where no swap is needed to achieve the maximum possible balanced substring
TEST(LongestBalancedTest, NoSwapNeeded) {
    Solution sol;
    EXPECT_EQ(sol.longestBalanced("0101"), 4);
    EXPECT_EQ(sol.longestBalanced("11001100"), 8);
}