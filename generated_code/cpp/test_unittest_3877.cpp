#include <gtest/gtest.h>
#include <vector>
#include <string>
#include "solution_proxy.h"

using namespace std;

class CardGameTest : public ::testing::Test {
protected:
    Solution sol;
};

/**
 * @brief Test standard provided examples or basic valid pairs.
 */
TEST_F(CardGameTest, StandardValidPairs) {
    // Example: "ax", "bx" are compatible (differ at index 0, both have 'x')
    vector<string> cards1 = {"ax", "bx", "cx", "dx"};
    char x1 = 'x';
    // Optimal: (ax, bx) and (cx, dx) -> 2 points
    EXPECT_EQ(sol.score(cards1, x1), 2);

    // Cards must contain x
    vector<string> cards2 = {"ab", "bb", "ax", "bx"};
    char x2 = 'x';
    // Only (ax, bx) contain 'x' and are compatible -> 1 point
    EXPECT_EQ(sol.score(cards2, x2), 1);
}

/**
 * @brief Test cases where cards are identical or too different to be compatible.
 */
TEST_F(CardGameTest, IncompatibleCards) {
    // Identical cards differ in 0 positions, so they are NOT compatible
    vector<string> cards1 = {"ax", "ax"};
    char x = 'x';
    EXPECT_EQ(sol.score(cards1, x), 0);

    // Differ in 2 positions
    vector<string> cards2 = {"ax", "by"};
    EXPECT_EQ(sol.score(cards2, x), 0);
}

/**
 * @brief Test maximum matching logic where choice matters.
 * This ensures the algorithm handles the "optimal play" constraint.
 */
TEST_F(CardGameTest, OptimalPlayMatching) {
    // "ax" is compatible with "bx" and "ay"
    // If we pair (ax, bx), we might prevent another pair.
    // In a graph of compatible cards containing x, we need Maximum Matching.
    vector<string> cards = {"ax", "bx", "ay", "by"};
    char x = 'a'; 
    // Cards containing 'a': "ax", "ay"
    // Compatible? Yes, differ at index 1.
    EXPECT_EQ(sol.score(cards, x), 1);
}

/**
 * @brief Test edge case: Empty input.
 */
TEST_F(CardGameTest, EmptyInput) {
    vector<string> cards = {};
    char x = 'z';
    EXPECT_EQ(sol.score(cards, x), 0);
}

/**
 * @brief Test edge case: No cards contain the character x.
 */
TEST_F(CardGameTest, NoTargetCharacterPresent) {
    vector<string> cards = {"ab", "bc", "cd"};
    char x = 'z';
    EXPECT_EQ(sol.score(cards, x), 0);
}

/**
 * @brief Test odd number of valid cards.
 */
TEST_F(CardGameTest, OddNumberOfValidCards) {
    vector<string> cards = {"ax", "bx", "cx"};
    char x = 'x';
    // Possible pairs: (ax, bx), (ax, cx), (bx, cx). Max 1 pair.
    EXPECT_EQ(sol.score(cards, x), 1);
}

/**
 * @brief Test constraint: Minimum input size.
 */
TEST_F(CardGameTest, SingleCard) {
    vector<string> cards = {"ax"};
    char x = 'x';
    EXPECT_EQ(sol.score(cards, x), 0);
}

/**
 * @brief Test cases where x is in different positions.
 */
TEST_F(CardGameTest, MixedPositionsOfX) {
    // "xa" and "xb" differ at index 1. Both contain 'x'.
    vector<string> cards = {"xa", "xb", "ax", "bx"};
    char x = 'x';
    // Pairs: (xa, xb) and (ax, bx) -> 2 points
    EXPECT_EQ(sol.score(cards, x), 2);
}