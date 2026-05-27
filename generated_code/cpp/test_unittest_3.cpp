#include <gtest/gtest.h>
#include <string>
#include "solution_3_1.cpp" // Note: Replace 'unknown' with the specific problem ID if available

class LongestSubstringTest : public ::testing::Test {
protected:
    Solution solution;
};

// --- Example Test Cases ---

TEST_F(LongestSubstringTest, Example1_NormalString) {
    std::string s = "abcabcbb";
    EXPECT_EQ(solution.lengthOfLongestSubstring(s), 3);
}

TEST_F(LongestSubstringTest, Example2_AllIdenticalCharacters) {
    std::string s = "bbbbb";
    EXPECT_EQ(solution.lengthOfLongestSubstring(s), 1);
}

TEST_F(LongestSubstringTest, Example3_SubstringWithRepeatingCharacter) {
    std::string s = "pwwkew";
    EXPECT_EQ(solution.lengthOfLongestSubstring(s), 3);
}

// --- Boundary and Edge Test Cases ---

TEST_F(LongestSubstringTest, EdgeCase_EmptyString) {
    std::string s = "";
    EXPECT_EQ(solution.lengthOfLongestSubstring(s), 0);
}

TEST_F(LongestSubstringTest, EdgeCase_SingleCharacter) {
    std::string s = "a";
    EXPECT_EQ(solution.lengthOfLongestSubstring(s), 1);
}

TEST_F(LongestSubstringTest, EdgeCase_AllUniqueCharacters) {
    std::string s = "abcdefg";
    EXPECT_EQ(solution.lengthOfLongestSubstring(s), 7);
}

TEST_F(LongestSubstringTest, Constraint_SpecialCharactersAndSpaces) {
    std::string s = "a b!@12 a";
    // Unique parts: "a b!@12 " (length 8) or " b!@12 a" (length 8)
    EXPECT_EQ(solution.lengthOfLongestSubstring(s), 8);
}

TEST_F(LongestSubstringTest, Constraint_AllSpaces) {
    std::string s = "    ";
    EXPECT_EQ(solution.lengthOfLongestSubstring(s), 1);
}

TEST_F(LongestSubstringTest, Structural_TwoRepeatedPatterns) {
    std::string s = "dvdf";
    // Substring "vdf" has length 3. Common pitfall for basic sliding window without correct index updates.
    EXPECT_EQ(solution.lengthOfLongestSubstring(s), 3);
}

TEST_F(LongestSubstringTest, Structural_LongestAtEnd) {
    std::string s = "abbaabcdef";
    EXPECT_EQ(solution.lengthOfLongestSubstring(s), 6); // "abcdef"
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}