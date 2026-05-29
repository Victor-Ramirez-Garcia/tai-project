#include <gtest/gtest.h>
#include <string>
#include "solution_proxy.h"

// Test Case for Example 1 provided in the problem description
TEST(DeciBinaryPartitionsTest, Example1) {
    Solution solution;
    std::string n = "32";
    EXPECT_EQ(solution.minPartitions(n), 3);
}

// Test Case for Example 2 provided in the problem description
TEST(DeciBinaryPartitionsTest, Example2) {
    Solution solution;
    std::string n = "82734";
    EXPECT_EQ(solution.minPartitions(n), 8);
}

// Test Case for Example 3 provided in the problem description
TEST(DeciBinaryPartitionsTest, Example3) {
    Solution solution;
    std::string n = "27346209830709182346";
    EXPECT_EQ(solution.minPartitions(n), 9);
}

// Edge Case: Minimum possible length of n (1 character) with minimum digit value
TEST(DeciBinaryPartitionsTest, MinimumLengthAndValue) {
    Solution solution;
    std::string n = "1";
    EXPECT_EQ(solution.minPartitions(n), 1);
}

// Edge Case: Minimum possible length of n (1 character) with maximum digit value
// This confirms a single maximum digit triggers the maximum possible response for a single character
TEST(DeciBinaryPartitionsTest, MinimumLengthMaximumValue) {
    Solution solution;
    std::string n = "9";
    EXPECT_EQ(solution.minPartitions(n), 9);
}

// Edge Case: Maximum possible length of n (10^5) consisting entirely of '1's
TEST(DeciBinaryPartitionsTest, MaximumLengthAllOnes) {
    Solution solution;
    std::string n(100000, '1');
    EXPECT_EQ(solution.minPartitions(n), 1);
}

// Edge Case: Maximum possible length of n (10^5) consisting entirely of '0's except the leading digit
TEST(DeciBinaryPartitionsTest, MaximumLengthAllZerosExceptFirst) {
    Solution solution;
    std::string n = "1" + std::string(99999, '0');
    EXPECT_EQ(solution.minPartitions(n), 1);
}

// Edge Case: Maximum possible length of n (10^5) ending with the maximum digit '9'
TEST(DeciBinaryPartitionsTest, MaximumLengthMaxDigitAtEnd) {
    Solution solution;
    std::string n = std::string(99999, '1') + "9";
    EXPECT_EQ(solution.minPartitions(n), 9);
}

// Edge Case: Maximum possible length of n (10^5) starting with the maximum digit '9'
TEST(DeciBinaryPartitionsTest, MaximumLengthMaxDigitAtStart) {
    Solution solution;
    std::string n = "9" + std::string(99999, '1');
    EXPECT_EQ(solution.minPartitions(n), 9);
}

// Verification Case: Checks that intermediate values (like 5) are handled correctly
TEST(DeciBinaryPartitionsTest, IntermediateDigitValue) {
    Solution solution;
    std::string n = "4523";
    EXPECT_EQ(solution.minPartitions(n), 5);
}