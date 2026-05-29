#include <gtest/gtest.h>
#include <string>
#include "solution_proxy.h"

// Test Case 1: Standard example provided in the problem description
TEST(SmallestPalindromeTest, ExampleTestCase) {
    Solution sol;
    std::string s = "abba";
    int k = 2;
    std::string expected = "baab";
    EXPECT_EQ(sol.smallestPalindrome(s, k), expected);
}

// Test Case 2: Requesting the 1st lexicographically smallest permutation
TEST(SmallestPalindromeTest, FirstPermutation) {
    Solution sol;
    std::string s = "abba";
    int k = 1;
    std::string expected = "abba";
    EXPECT_EQ(sol.smallestPalindrome(s, k), expected);
}

// Test Case 3: k exceeds the number of total distinct palindromic permutations
TEST(SmallestPalindromeTest, KExceedsTotalPermutations) {
    Solution sol;
    std::string s = "abba";
    int k = 3;
    std::string expected = "";
    EXPECT_EQ(sol.smallestPalindrome(s, k), expected);
}

// Test Case 4: Input string itself cannot form any palindrome
TEST(SmallestPalindromeTest, NotAPalindrome) {
    Solution sol;
    std::string s = "abc";
    int k = 1;
    std::string expected = "";
    EXPECT_EQ(sol.smallestPalindrome(s, k), expected);
}

// Test Case 5: Single character string (Minimum input size edge case)
TEST(SmallestPalindromeTest, SingleCharacterString) {
    Solution sol;
    std::string s = "a";
    int k = 1;
    std::string expected = "a";
    EXPECT_EQ(sol.smallestPalindrome(s, k), expected);
    
    // k = 2 should return empty since only 1 permutation exists
    EXPECT_EQ(sol.smallestPalindrome(s, 2), "");
}

// Test Case 6: Empty string input edge case
TEST(SmallestPalindromeTest, EmptyString) {
    Solution sol;
    std::string s = "";
    int k = 1;
    std::string expected = "";
    EXPECT_EQ(sol.smallestPalindrome(s, k), expected);
}

// Test Case 7: Palindrome with an odd length (contains a single center character)
TEST(SmallestPalindromeTest, OddLengthPalindrome) {
    Solution sol;
    std::string s = "ababa"; // Half characters: 'a':2, 'b':0 (plus 'b' in middle). Permutations of "aa": "aa"
    // Total palindromes: "aabaa" (only 1 distinct palindrome)
    EXPECT_EQ(sol.smallestPalindrome(s, 1), "aabaa");
    EXPECT_EQ(sol.smallestPalindrome(s, 2), "");
}

// Test Case 8: Multi-character permutations to verify lexicographical sorting order
TEST(SmallestPalindromeTest, LexicographicalOrdering) {
    Solution sol;
    std::string s = "aabbcc"; // Half characters: 'a':1, 'b':1, 'c':1. Half permutations: "abc", "acb", "bac", "bca", "cab", "cba"
    
    EXPECT_EQ(sol.smallestPalindrome(s, 1), "abccba");
    EXPECT_EQ(sol.smallestPalindrome(s, 2), "acbbca");
    EXPECT_EQ(sol.smallestPalindrome(s, 3), "baccab");
    EXPECT_EQ(sol.smallestPalindrome(s, 6), "cbaabc");
    EXPECT_EQ(sol.smallestPalindrome(s, 7), "");
}

// Test Case 9: Duplicate characters where identity counts as one distinct rearrangement
TEST(SmallestPalindromeTest, DuplicateCharacters) {
    Solution sol;
    std::string s = "aaaa"; // Only 1 unique palindromic permutation: "aaaa"
    EXPECT_EQ(sol.smallestPalindrome(s, 1), "aaaa");
    EXPECT_EQ(sol.smallestPalindrome(s, 2), "");
}