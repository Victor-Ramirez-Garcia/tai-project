#include <gtest/gtest.h>
#include <string>
#include "solution_proxy.h"

// Test Case 1: Example 1 from standard problem description (s = "hello")
// |'h' - 'e'| + |'e' - 'l'| + |'l' - 'l'| + |'l' - 'o'| = 104-101 + 101-108 + 108-108 + 108-111 = 3 + 7 + 0 + 3 = 13
TEST(SolutionTest, Example1_Hello) {
    Solution solution;
    std::string s = "hello";
    EXPECT_EQ(solution.scoreOfString(s), 13);
}

// Test Case 2: Example 2 from standard problem description (s = "zaz")
// |'z' - 'a'| + |'a' - 'z'| = 122-97 + 97-122 = 25 + 25 = 50
TEST(SolutionTest, Example2_Zaz) {
    Solution solution;
    std::string s = "zaz";
    EXPECT_EQ(solution.scoreOfString(s), 50);
}

// Test Case 3: Minimum length constraint (s.length == 2)
TEST(SolutionTest, MinimumLength) {
    Solution solution;
    std::string s = "ab"; // |97 - 98| = 1
    EXPECT_EQ(solution.scoreOfString(s), 1);
}

// Test Case 4: Identical characters (Score should be 0)
TEST(SolutionTest, IdenticalCharacters) {
    Solution solution;
    std::string s = "aaaaa";
    EXPECT_EQ(solution.scoreOfString(s), 0);
}

// Test Case 5: Maximum length constraint (s.length == 100)
TEST(SolutionTest, MaximumLength) {
    Solution solution;
    std::string s(100, 'a'); // 100 'a's, score should be 0
    EXPECT_EQ(solution.scoreOfString(s), 0);
}

// Test Case 6: Alternating maximum ASCII differences ('a' and 'z')
TEST(SolutionTest, MaxAsciiDifferences) {
    Solution solution;
    std::string s = "azaz"; // |97-122| + |122-97| + |97-122| = 25 + 25 + 25 = 75
    EXPECT_EQ(solution.scoreOfString(s), 75);
}

// Test Case 7: Strictly increasing ASCII values
TEST(SolutionTest, StrictlyIncreasing) {
    Solution solution;
    std::string s = "abcdef"; // 1 + 1 + 1 + 1 + 1 = 5
    EXPECT_EQ(solution.scoreOfString(s), 5);
}