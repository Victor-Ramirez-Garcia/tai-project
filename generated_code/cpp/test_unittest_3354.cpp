#include <gtest/gtest.h>
#include <string>
#include "solution_proxy.h"

// Test Case 1: Example 1 - Basic substitution to minimize cost
TEST(MinimizeStringValueTest, Example1) {
    Solution sol;
    std::string s = "???";
    // Each '?' should ideally pick different characters to keep cost 0.
    // Lexicographically smallest choice is "abc".
    std::string expected = "abc";
    EXPECT_EQ(sol.minimizeStringValue(s), expected);
}

// Test Case 2: Example 2 - Handling existing characters and tie-breaking
TEST(MinimizeStringValueTest, Example2) {
    Solution sol;
    std::string s = "a?b?";
    // Initial frequencies: a:1, b:1. 
    // To minimize cost, the two '?' should fill the next lowest available slots.
    // The next lowest frequencies available are for other letters like 'c', 'd', etc.
    // Sorted placement ensures the lexicographically smallest result.
    std::string expected = "acbd";
    EXPECT_EQ(sol.minimizeStringValue(s), expected);
}

// Test Case 3: Minimum constraints - Single character that is a letter
TEST(MinimizeStringValueTest, MinimumSizeNoQuestionMark) {
    Solution sol;
    std::string s = "z";
    std::string expected = "z";
    EXPECT_EQ(sol.minimizeStringValue(s), expected);
}

// Test Case 4: Minimum constraints - Single character that is a question mark
TEST(MinimizeStringValueTest, MinimumSizeWithQuestionMark) {
    Solution sol;
    std::string s = "?";
    std::string expected = "a";
    EXPECT_EQ(sol.minimizeStringValue(s), expected);
}

// Test Case 5: All characters present, high frequencies forcing costs > 0
TEST(MinimizeStringValueTest, AllLettersPresentRepeated) {
    Solution sol;
    // Every lowercase letter from 'a' to 'z' repeated twice, plus '?'
    std::string s = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz?";
    // '?' should pick the letter that maintains the minimum total cost, 
    // and to be lexicographically smallest, it must be 'a'.
    std::string expected = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza";
    EXPECT_EQ(sol.minimizeStringValue(s), expected);
}

// Test Case 6: Multiple '?' requiring tracking frequency increases dynamically
TEST(MinimizeStringValueTest, MultipleQuestionMarksFrequencyBalance) {
    Solution sol;
    std::string s = "a???b";
    // Initial: a:1, b:1. 
    // The three '?' will be assigned to 'c', 'd', 'e' to keep individual costs at 0.
    // Placed in sorted order at the '?' positions: "acdeb"
    std::string expected = "acdeb";
    EXPECT_EQ(sol.minimizeStringValue(s), expected);
}

// Test Case 7: Lexicographical sorting requirement for replacements
TEST(MinimizeStringValueTest, LexicographicalSortingOfReplacements) {
    Solution sol;
    // The '?' positions are at the end and the beginning
    std::string s = "?z?";
    // The best characters to insert are 'a' and 'b'.
    // They must be sorted as 'a' then 'b' and placed into the '?' positions from left to right.
    std::string expected = "azb";
    EXPECT_EQ(sol.minimizeStringValue(s), expected);
}