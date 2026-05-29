#include <gtest/gtest.h>
#include <vector>
#include <string>
#include "solution_proxy.h"

using namespace std;

class MaxScoreWordsTest : public ::testing::Test {
protected:
    Solution solution;
    
    // Helper to generate a default score vector with zeros
    vector<int> getZeroScore() {
        return vector<int>(26, 0);
    }
};

// Test Case: Example 1 from problem description
TEST_F(MaxScoreWordsTest, Example1) {
    vector<string> words = {"dog", "cat", "dad", "good"};
    vector<char> letters = {'a', 'a', 'c', 'd', 'd', 'd', 'g', 'o', 'o'};
    vector<int> score = {1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0};
    
    EXPECT_EQ(solution.maxScoreWords(words, letters, score), 23);
}

// Test Case: Example 2 from problem description
TEST_F(MaxScoreWordsTest, Example2) {
    vector<string> words = {"xxxz", "ax", "bx", "cx"};
    vector<char> letters = {'z', 'a', 'b', 'c', 'x', 'x', 'x'};
    vector<int> score = {4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10};
    
    EXPECT_EQ(solution.maxScoreWords(words, letters, score), 27);
}

// Test Case: Example 3 from problem description (insufficient frequency of a letter)
TEST_F(MaxScoreWordsTest, Example3) {
    vector<string> words = {"leetcode"};
    vector<char> letters = {'l', 'e', 't', 'c', 'o', 'd'};
    vector<int> score = {0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0};
    
    EXPECT_EQ(solution.maxScoreWords(words, letters, score), 0);
}

// Edge Case: Minimum constraints (1 word, 1 letter, matching)
TEST_F(MaxScoreWordsTest, MinimumConstraintsMatch) {
    vector<string> words = {"a"};
    vector<char> letters = {'a'};
    vector<int> score = getZeroScore();
    score[0] = 10; // 'a' has a score of 10
    
    EXPECT_EQ(solution.maxScoreWords(words, letters, score), 10);
}

// Edge Case: Minimum constraints (1 word, 1 letter, mismatch)
TEST_F(MaxScoreWordsTest, MinimumConstraintsMismatch) {
    vector<string> words = {"a"};
    vector<char> letters = {'b'};
    vector<int> score = getZeroScore();
    score[0] = 10;
    score[1] = 5;
    
    EXPECT_EQ(solution.maxScoreWords(words, letters, score), 0);
}

// Edge Case: No words can be formed because letters are entirely missing
TEST_F(MaxScoreWordsTest, EmptyIntersectionLetters) {
    vector<string> words = {"hello", "world"};
    vector<char> letters = {'a', 'b', 'c', 'z'};
    vector<int> score = getZeroScore();
    fill(score.begin(), score.end(), 10); // Even with max score, should be 0
    
    EXPECT_EQ(solution.maxScoreWords(words, letters, score), 0);
}

// Edge Case: All scores are zero, output must be zero regardless of formation
TEST_F(MaxScoreWordsTest, AllScoresZero) {
    vector<string> words = {"dog", "cat", "bird"};
    vector<char> letters = {'d', 'o', 'g', 'c', 'a', 't', 'b', 'i', 'r', 'd'};
    vector<int> score = getZeroScore(); 
    
    EXPECT_EQ(solution.maxScoreWords(words, letters, score), 0);
}

// Edge Case: Abundant letters, multiple combinations possible, choose highest value subsets
TEST_F(MaxScoreWordsTest, SelectHighestValueCombination) {
    vector<string> words = {"apple", "banana", "cherry"};
    // Abundant letters available to form any combinations, but maybe not all simultaneously
    vector<char> letters = {'a', 'p', 'p', 'l', 'e', 'b', 'a', 'n', 'a', 'n', 'a', 'c', 'h', 'e', 'r', 'r', 'y'};
    vector<int> score = getZeroScore();
    score[0] = 2;  // a
    score[1] = 3;  // b
    score[2] = 5;  // c
    score[4] = 1;  // e
    score[7] = 4;  // h
    score[11] = 2; // l
    score[13] = 2; // n
    score[15] = 3; // p
    score[17] = 4; // r
    score[24] = 6; // y
    
    // Scores: 
    // apple = 2 + 3 + 3 + 2 + 1 = 11
    // banana = 3 + 2 + 2 + 2 + 2 + 2 = 13
    // cherry = 5 + 4 + 1 + 4 + 4 + 6 = 24
    // letters array has enough for banana + cherry, or apple + cherry, or apple + banana.
    // Let's verify letters for banana + cherry: 
    // Requires: b(1), a(3), n(2), c(1), h(1), e(1), r(2), y(1). Included in letters.
    // Total max score = 13 + 24 = 37.
    
    EXPECT_EQ(solution.maxScoreWords(words, letters, score), 37);
}

// Edge Case: Word length constraint maximums (14 words, 15 chars each)
TEST_F(MaxScoreWordsTest, MaximumWordsAndLengthConstraints) {
    // 14 words, each of length 15 filled with 'a'
    vector<string> words(14, string(15, 'a')); 
    // 100 letters of 'a'
    vector<char> letters(100, 'a');
    vector<int> score = getZeroScore();
    score[0] = 1; // each 'a' is worth 1 point
    
    // Each word takes 15 'a's. 100 / 15 = 6 words can be fully formed.
    // Total score = 6 words * 15 chars * 1 point = 90.
    EXPECT_EQ(solution.maxScoreWords(words, letters, score), 90);
}

// Edge Case: Letters constraint maximum (100 elements) but all unique/unusable
TEST_F(MaxScoreWordsTest, MaxLettersButUnusable) {
    vector<string> words = {"zzzzz"};
    vector<char> letters(100, 'a'); // 100 'a's, but we need 'z'
    vector<int> score = getZeroScore();
    score[0] = 10;
    score[25] = 10;
    
    EXPECT_EQ(solution.maxScoreWords(words, letters, score), 0);
}