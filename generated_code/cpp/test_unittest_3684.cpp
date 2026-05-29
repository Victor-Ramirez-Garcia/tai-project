#include <gtest/gtest.h>
#include <string>
#include "solution_proxy.h"

using namespace std;

// Test case for a standard match where '*' is replaced by an empty string
TEST(HasMatchTest, EmptyStarReplacement) {
    Solution sol;
    // 'a' + '' + 'b' -> 'ab' is a substring of 'leetcodeabc'
    EXPECT_TRUE(sol.hasMatch("leetcodeabc", "a*b"));
}

// Test case for a standard match where '*' is replaced by multiple characters
TEST(HasMatchTest, MultiCharStarReplacement) {
    Solution sol;
    // 'l' + 'eetco' + 'd' -> 'leetcod' is a substring of 'leetcode'
    EXPECT_TRUE(sol.hasMatch("leetcode", "l*d"));
}

// Test case where the pattern cannot be formed as a substring
TEST(HasMatchTest, NoMatchPossible) {
    Solution sol;
    // 'b' occurs before 'a' in the pattern, but not in 'leetcode'
    EXPECT_FALSE(sol.hasMatch("leetcode", "b*a"));
}

// Test case for the minimum allowed length constraint (s.length = 1, p.length = 1)
TEST(HasMatchTest, MinimumLengthConstraints) {
    Solution sol;
    // p contains exactly one '*' which can match the entire string 'a' as an empty string
    EXPECT_TRUE(sol.hasMatch("a", "*"));
}

// Test case where '*' is at the very beginning of the pattern
TEST(HasMatchTest, StarAtStartOfPattern) {
    Solution sol;
    EXPECT_TRUE(sol.hasMatch("leetcode", "*de"));
    EXPECT_FALSE(sol.hasMatch("leetcode", "*xyz"));
}

// Test case where '*' is at the very end of the pattern
TEST(HasMatchTest, StarAtEndOfPattern) {
    Solution sol;
    EXPECT_TRUE(sol.hasMatch("leetcode", "lee*"));
    EXPECT_FALSE(sol.hasMatch("leetcode", "xyz*"));
}

// Test case handling overlapping characters or repeated segments in the string
TEST(HasMatchTest, OverlappingAndRepeatedCharacters) {
    Solution sol;
    // Prefix 'a' and suffix 'a' must be distinct non-overlapping occurrences if p expects it
    EXPECT_TRUE(sol.hasMatch("aaaaa", "a*a"));
    EXPECT_TRUE(sol.hasMatch("ab", "a*b"));
    EXPECT_FALSE(sol.hasMatch("a", "a*a")); 
}

// Test case verifying behavior near maximum constraint boundaries (length 50)
TEST(HasMatchTest, MaximumLengthConstraints) {
    Solution sol;
    string max_s(50, 'a');
    string max_p(49, 'a');
    max_p += "*";
    
    EXPECT_TRUE(sol.hasMatch(max_s, max_p));
    EXPECT_FALSE(sol.hasMatch(string(48, 'a'), max_p));
}