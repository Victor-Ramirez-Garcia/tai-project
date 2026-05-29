#include <gtest/gtest.h>
#include <string>
#include "solution_proxy.h"

// Test Case for the provided example in the problem statement
TEST(MaxDistinctSubstringsTest, ExampleCase) {
    Solution sol;
    std::string s = "abab";
    // Expected output is 2 by splitting into "a" and "bab"
    EXPECT_EQ(sol.maxDistinct(s), 2);
}

// Test Case for the minimum length string constraint (Single character)
TEST(MaxDistinctSubstringsTest, SingleCharacterString) {
    Solution sol;
    std::string s = "a";
    EXPECT_EQ(sol.maxDistinct(s), 1);
}

// Test Case where all characters in the string are identical
// Any split will result in substrings starting with the same character, except the first one.
TEST(MaxDistinctSubstringsTest, AllIdenticalCharacters) {
    Solution sol;
    std::string s = "aaaaaa";
    EXPECT_EQ(sol.maxDistinct(s), 1);
}

// Test Case where all characters are already distinct
// The string can be split into individual characters, maximizing the count.
TEST(MaxDistinctSubstringsTest, AllDistinctCharacters) {
    Solution sol;
    std::string s = "abcdefg";
    EXPECT_EQ(sol.maxDistinct(s), 7);
}

// Test Case for a string with repeating patterns where maximizing splits requires careful partitioning
TEST(MaxDistinctSubstringsTest, AlternatingCharactersLonger) {
    Solution sol;
    std::string s = "abcabc";
    // Can be split into "a", "b", "cabc" -> 3 distinct starting characters ('a', 'b', 'c')
    EXPECT_EQ(sol.maxDistinct(s), 3);
}

// Test Case where the unique characters appear at the very end of a long repeating sequence
TEST(MaxDistinctSubstringsTest, UniqueCharactersAtEnd) {
    Solution sol;
    std::string s = "aaaaazbc";
    // Can be split into "aaaaaz", "b", "c" -> 3 distinct starting characters ('a', 'b', 'c')
    EXPECT_EQ(sol.maxDistinct(s), 3);
}