#include <gtest/gtest.h>
#include <string>
#include "solution_proxy.h"

// Test Case 1: Provided Examples in the Problem Description
TEST(StrongPasswordCheckerTest, ProvidedExamples) {
    Solution tester;
    
    // Example 1: Too short, missing uppercase and digit
    EXPECT_EQ(tester.strongPasswordChecker("a"), 5);
    
    // Example 2: Too short, has lowercase, uppercase, and digit
    EXPECT_EQ(tester.strongPasswordChecker("aA1"), 3);
    
    // Example 3: Already strong
    EXPECT_EQ(tester.strongPasswordChecker("1337C0d3"), 0);
}

// Test Case 2: Edge Cases for Short Passwords (< 6 characters)
TEST(StrongPasswordCheckerTest, ShortPasswords) {
    Solution tester;
    
    // Empty string (Minimum constraint edge case)
    EXPECT_EQ(tester.strongPasswordChecker(""), 6);
    
    // Length 5, missing types
    EXPECT_EQ(tester.strongPasswordChecker("aaaaa"), 2);
    
    // Length 5, has all types but needs 1 insertion to reach length 6
    EXPECT_EQ(tester.strongPasswordChecker("aA1!#"), 1);
}

// Test Case 3: Edge Cases for Long Passwords (> 20 characters)
TEST(StrongPasswordCheckerTest, LongPasswords) {
    Solution tester;
    
    // Length 21, all repeating, needs deletions and replacements
    EXPECT_EQ(tester.strongPasswordChecker("AAAAAAAAAAAAAAAAAAAAA"), 7);
    
    // Length 22, valid types but too long with repeating sequences
    EXPECT_EQ(tester.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaaa"), 8);
    
    // Long password requiring strictly deletions to meet the length constraint
    EXPECT_EQ(tester.strongPasswordChecker("abababababababababababab"), 4);
}

// Test Case 4: Character Type Requirements (Length is valid, but missing types)
TEST(StrongPasswordCheckerTest, MissingCharacterTypes) {
    Solution tester;
    
    // Length valid, all lowercase
    EXPECT_EQ(tester.strongPasswordChecker("abcdefg"), 2);
    
    // Length valid, lowercase and uppercase, missing digit
    EXPECT_EQ(tester.strongPasswordChecker("ABCdefg"), 1);
    
    // Length valid, uppercase and digits, missing lowercase
    EXPECT_EQ(tester.strongPasswordChecker("ABC1234"), 1);
}

// Test Case 5: Repeating Characters (Length valid, types valid, but has triplets)
TEST(StrongPasswordCheckerTest, RepeatingCharacters) {
    Solution tester;
    
    // Contains one triplet "aaa", can be fixed with 1 replacement
    EXPECT_EQ(tester.strongPasswordChecker("aaaA1!"), 1);
    
    // Contains multiple repeating groups
    EXPECT_EQ(tester.strongPasswordChecker("baaaaA111"), 2);
}

// Test Case 6: Exact Length Constraints (Boundaries of 6 and 20)
TEST(StrongPasswordCheckerTest, BoundaryLengths) {
    Solution tester;
    
    // Exact minimum length 6, already strong
    EXPECT_EQ(tester.strongPasswordChecker("aA1234"), 0);
    
    // Exact maximum length 20, already strong
    EXPECT_EQ(tester.strongPasswordChecker("aA1bcdefghijklmnopq"), 0);
}