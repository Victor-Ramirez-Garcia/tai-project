#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

// Test case for Example 1 from the problem description
TEST(PutMarblesTest, Example1) {
    Solution solution;
    vector<int> weights = {1, 3, 5, 1};
    int k = 2;
    long long expected = 4;
    EXPECT_EQ(solution.putMarbles(weights, k), expected);
}

// Test case for Example 2 from the problem description
TEST(PutMarblesTest, Example2) {
    Solution solution;
    vector<int> weights = {1, 3};
    int k = 2;
    long long expected = 0;
    EXPECT_EQ(solution.putMarbles(weights, k), expected);
}

// Edge case: Minimum allowed inputs (k = 1, small array)
// When k = 1, there is only one way to distribute all marbles into one bag.
// The max and min scores will be identical, resulting in a difference of 0.
TEST(PutMarblesTest, MinimumKValue) {
    Solution solution;
    vector<int> weights = {1, 3, 5, 1};
    int k = 1;
    long long expected = 0;
    EXPECT_EQ(solution.putMarbles(weights, k), expected);
}

// Edge case: k equals the number of elements in the weights array
// Every marble gets its own bag. There is only one unique distribution,
// so the difference between max and min scores is 0.
TEST(PutMarblesTest, KEqualsArrayLength) {
    Solution solution;
    vector<int> weights = {5, 4, 3, 2, 1};
    int k = 5;
    long long expected = 0;
    EXPECT_EQ(solution.putMarbles(weights, k), expected);
}

// Edge case: All weights are identical
// Any distribution strategy yields the same score, so the difference is 0.
TEST(PutMarblesTest, IdenticalWeights) {
    Solution solution;
    vector<int> weights = {2, 2, 2, 2, 2};
    int k = 3;
    long long expected = 0;
    EXPECT_EQ(solution.putMarbles(weights, k), expected);
}

// Performance/Scalability Case: Larger input to ensure handling of 64-bit integer values (long long)
// Ensure no integer overflow happens during internal pairings or calculations.
TEST(PutMarblesTest, LargeWeightsAvoidOverflow) {
    Solution solution;
    vector<int> weights = {1000000000, 1000000000, 1000000000, 1000000000};
    int k = 2;
    long long expected = 0;
    EXPECT_EQ(solution.putMarbles(weights, k), expected);
}

// General case: Multiple elements with varying weight fluctuations to verify the sorting behavior
TEST(PutMarblesTest, GeneralFluctuatingWeights) {
    Solution solution;
    vector<int> weights = {1, 5, 2, 8, 3, 7};
    int k = 3;
    // Pairs sums: 1+5=6, 5+2=7, 2+8=10, 8+3=11, 3+7=10 -> Sorted: 6, 7, 10, 10, 11
    // For k=3, we need to pick k-1 = 2 pairs.
    // Max sum pairs: 11 + 10 = 21
    // Min sum pairs: 6 + 7 = 13
    // Expected difference: 21 - 13 = 8
    long long expected = 8;
    EXPECT_EQ(solution.putMarbles(weights, k), expected);
}