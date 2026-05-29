#include <gtest/gtest.h>
#include <string>
#include "solution_proxy.h"

// Test Case: Example 1 from the problem description ("abcc" -> true)
TEST(EqualFrequencyTest, Example1_RemoveOneOfDuplicate) {
    Solution solution;
    std::string word = "abcc";
    EXPECT_TRUE(solution.equalFrequency(word));
}

// Test Case: Example 2 from the problem description ("aazz" -> false)
TEST(EqualFrequencyTest, Example2_BalancedFrequencies) {
    Solution solution;
    std::string word = "aazz";
    EXPECT_FALSE(solution.equalFrequency(word));
}

// Edge Case: Minimum constraints (String length 2) - same characters ("aa" -> true)
TEST(EqualFrequencyTest, EdgeCase_MinLength_SameChars) {
    Solution solution;
    std::string word = "aa";
    EXPECT_TRUE(solution.equalFrequency(word));
}

// Edge Case: Minimum constraints (String length 2) - distinct characters ("ab" -> true)
TEST(EqualFrequencyTest, EdgeCase_MinLength_DistinctChars) {
    Solution solution;
    std::string word = "ab";
    EXPECT_TRUE(solution.equalFrequency(word));
}

// Edge Case: All characters have a frequency of 1 ("abcdefg" -> true)
TEST(EqualFrequencyTest, AllUniqueCharacters) {
    Solution solution;
    std::string word = "abcdefg";
    EXPECT_TRUE(solution.equalFrequency(word));
}

// Edge Case: One character appears once, all others appear multiple times equally ("abbcc" -> true)
TEST(EqualFrequencyTest, RemoveSingleOccurrenceCharacter) {
    Solution solution;
    std::string word = "abbcc";
    EXPECT_TRUE(solution.equalFrequency(word));
}

// Edge Case: One character appears N+1 times, all others appear N times ("aabbccc" -> true)
TEST(EqualFrequencyTest, RemoveFromHighestFrequency) {
    Solution solution;
    std::string word = "aabbccc";
    EXPECT_TRUE(solution.equalFrequency(word));
}

// Edge Case: Impossible configuration where removing one doesn't balance the rest ("aaabbbccc" -> false)
TEST(EqualFrequencyTest, BalancedButHigherThanTwo) {
    Solution solution;
    std::string word = "aaabbbccc";
    EXPECT_FALSE(solution.equalFrequency(word));
}

// Edge Case: Single character type repeating multiple times ("aaaaa" -> true)
TEST(EqualFrequencyTest, SingleCharacterRepeating) {
    Solution solution;
    std::string word = "aaaaa";
    EXPECT_TRUE(solution.equalFrequency(word));
}

// Edge Case: Frequencies are close but mathematically impossible to balance ("aabbccddde" -> false)
TEST(EqualFrequencyTest, MultipleFrequencyAnomalies) {
    Solution solution;
    std::string word = "aabbccddde";
    EXPECT_FALSE(solution.equalFrequency(word));
}