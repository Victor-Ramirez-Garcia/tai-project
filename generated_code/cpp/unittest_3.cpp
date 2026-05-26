#include <gtest/gtest.h>
#include <string>
#include <algorithm>

// The Solution class as provided in the problem statement
class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        int n = s.length();
        int maxLength = 0;
        int start = 0;
        int charMap[128] = {0}; // Covers ASCII for letters, digits, symbols, and spaces

        for (int end = 0; end < n; end++) {
            start = std::max(start, charMap[(int)s[end]]);
            maxLength = std::max(maxLength, end - start + 1);
            charMap[(int)s[end]] = end + 1;
        }
        return maxLength;
    }
};

// Test Suite for Longest Substring Without Repeating Characters
class LongestSubstringTest : public ::testing::Test {
protected:
    Solution solution;
};

// Example 1 from problem description
TEST_F(LongestSubstringTest, Example1_StandardCase) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("abcabcbb"), 3);
}

// Example 2 from problem description
TEST_F(LongestSubstringTest, Example2_RepeatedCharacters) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("bbbbb"), 1);
}

// Example 3 from problem description
TEST_F(LongestSubstringTest, Example3_MixedCharacters) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("pwwkew"), 3);
}

// Edge Case: Empty String (Min constraint: s.length = 0)
TEST_F(LongestSubstringTest, EdgeCase_EmptyString) {
    EXPECT_EQ(solution.lengthOfLongestSubstring(""), 0);
}

// Edge Case: Single Character
TEST_F(LongestSubstringTest, EdgeCase_SingleCharacter) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("a"), 1);
}

// Edge Case: All unique characters
TEST_F(LongestSubstringTest, EdgeCase_AllUniqueCharacters) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("abcdefg"), 7);
}

// Constraint Case: Symbols and Spaces
TEST_F(LongestSubstringTest, ConstraintCase_SymbolsAndSpaces) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("a b c !@# a "), 7); // " b c !@#" or "b c !@# "
}

// Constraint Case: Longest substring at the very end
TEST_F(LongestSubstringTest, EdgeCase_LongestAtEnd) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("aabbcde"), 4); // "bcde"
}

// Constraint Case: Digits
TEST_F(LongestSubstringTest, ConstraintCase_Digits) {
    EXPECT_EQ(solution.lengthOfLongestSubstring("123123456"), 6); // "123456"
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}