#include <gtest/gtest.h>
#include <string>
#include "program_3_1.cpp"

class LongestSubstringTest : public ::testing::Test {
protected:
    Solution sol;
};

// --- Example Cases ---

TEST_F(LongestSubstringTest, Example1_StandardString) {
    std::string s = "abcabcbb";
    EXPECT_EQ(sol.lengthOfLongestSubstring(s), 3);
}

TEST_F(LongestSubstringTest, Example2_AllIdentical) {
    std::string s = "bbbbb";
    EXPECT_EQ(sol.lengthOfLongestSubstring(s), 1);
}

TEST_F(LongestSubstringTest, Example3_MixedCharacters) {
    std::string s = "pwwkew";
    EXPECT_EQ(sol.lengthOfLongestSubstring(s), 3);
}

// --- Edge Cases & Constraints ---

TEST_F(LongestSubstringTest, EmptyString) {
    std::string s = "";
    EXPECT_EQ(sol.lengthOfLongestSubstring(s), 0);
}

TEST_F(LongestSubstringTest, SingleCharacter) {
    std::string s = "a";
    EXPECT_EQ(sol.lengthOfLongestSubstring(s), 1);
}

TEST_F(LongestSubstringTest, TwoIdenticalCharacters) {
    std::string s = "aa";
    EXPECT_EQ(sol.lengthOfLongestSubstring(s), 1);
}

TEST_F(LongestSubstringTest, LongestIsAtStart) {
    std::string s = "abcdefghijaa";
    EXPECT_EQ(sol.lengthOfLongestSubstring(s), 10);
}

TEST_F(LongestSubstringTest, LongestIsAtEnd) {
    std::string s = "aabbcdefghij";
    EXPECT_EQ(sol.lengthOfLongestSubstring(s), 8);
}

TEST_F(LongestSubstringTest, SymbolsAndSpaces) {
    std::string s = "a b!@#$ %^&*()";
    // Unique characters including space and symbols
    EXPECT_EQ(sol.lengthOfLongestSubstring(s), 14);
}

TEST_F(LongestSubstringTest, DigitsOnly) {
    std::string s = "123123456";
    EXPECT_EQ(sol.lengthOfLongestSubstring(s), 6);
}

TEST_F(LongestSubstringTest, MaxLengthConstraintSimulation) {
    // Generate a repeating pattern to simulate heavy load
    std::string s = "";
    std::string pattern = "abcdefghijklmnopqrstuvwxyz";
    for(int i = 0; i < 1000; ++i) {
        s += pattern;
    }
    // Length is 26,000, within 5 * 10^4. Longest unique should be 26.
    EXPECT_EQ(sol.lengthOfLongestSubstring(s), 26);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}