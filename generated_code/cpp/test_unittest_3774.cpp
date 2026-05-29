#include <gtest/gtest.h>
#include <string>
#include "solution_proxy.h"

// Test case for a standard example where the reduction results in identical digits
TEST(HasSameDigitsTest, ExampleTrueCase) {
    Solution solution;
    // Example: "3902" -> "292" -> "11" -> true
    EXPECT_TRUE(solution.hasSameDigits("3902"));
}

// Test case for a standard example where the reduction results in different digits
TEST(HasSameDigitsTest, ExampleFalseCase) {
    Solution solution;
    // Example: "346" -> "70" -> false
    EXPECT_FALSE(solution.hasSameDigits("346"));
}

// Edge Case: Minimum possible length for the input string (exactly 2 digits)
TEST(HasSameDigitsTest, MinimumLengthTrue) {
    Solution solution;
    EXPECT_TRUE(solution.hasSameDigits("77"));
}

TEST(HasSameDigitsTest, MinimumLengthFalse) {
    Solution solution;
    EXPECT_FALSE(solution.hasSameDigits("78"));
}

// Edge Case: All identical digits in the initial string
TEST(HasSameDigitsTest, AllIdenticalDigits) {
    Solution solution;
    // "5555" -> "000" -> "00" -> true
    EXPECT_TRUE(solution.hasSameDigits("5555"));
}

// Edge Case: Alternating digits that cancel out or reduce symmetrically
TEST(HasSameDigitsTest, SymmetricalReduction) {
    Solution solution;
    // "1212" -> "333" -> "66" -> true
    EXPECT_TRUE(solution.hasSameDigits("1212"));
}

// Edge Case: Large input reduction producing true
TEST(HasSameDigitsTest, LargeInputTrue) {
    Solution solution;
    // "11111" -> "2222" -> "444" -> "88" -> true
    EXPECT_TRUE(solution.hasSameDigits("11111"));
}

// Edge Case: Large input reduction producing false
TEST(HasSameDigitsTest, LargeInputFalse) {
    Solution solution;
    // "12345" -> "3579" -> "826" -> "08" -> false
    EXPECT_FALSE(solution.hasSameDigits("12345"));
}

// Edge Case: Leading zeros or multiple zeros in the string
TEST(HasSameDigitsTest, StringWithZeros) {
    Solution solution;
    // "000" -> "00" -> true
    EXPECT_TRUE(solution.hasSameDigits("000"));
    // "090" -> "99" -> true
    EXPECT_TRUE(solution.hasSameDigits("090"));
}