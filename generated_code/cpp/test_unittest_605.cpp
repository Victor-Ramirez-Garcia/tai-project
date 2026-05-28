#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

// Test Case 1: Provided Example 1 - Single flower can be placed in the middle
TEST(CanPlaceFlowersTest, ExampleOne) {
    Solution sol;
    vector<int> flowerbed = {1, 0, 0, 0, 1};
    int n = 1;
    EXPECT_TRUE(sol.canPlaceFlowers(flowerbed, n));
}

// Test Case 2: Provided Example 2 - Too many flowers to place
TEST(CanPlaceFlowersTest, ExampleTwo) {
    Solution sol;
    vector<int> flowerbed = {1, 0, 0, 0, 1};
    int n = 2;
    EXPECT_FALSE(sol.canPlaceFlowers(flowerbed, n));
}

// Test Case 3: Requesting 0 flowers should always return true
TEST(CanPlaceFlowersTest, ZeroFlowersRequested) {
    Solution sol;
    vector<int> flowerbed = {1, 0, 1, 0, 1};
    int n = 0;
    EXPECT_TRUE(sol.canPlaceFlowers(flowerbed, n));
}

// Test Case 4: Absolute minimum size (length = 1) - Empty plot, place 1
TEST(CanPlaceFlowersTest, SingleEmptyPlotSuccess) {
    Solution sol;
    vector<int> flowerbed = {0};
    int n = 1;
    EXPECT_TRUE(sol.canPlaceFlowers(flowerbed, n));
}

// Test Case 5: Absolute minimum size (length = 1) - Empty plot, place 0
TEST(CanPlaceFlowersTest, SingleEmptyPlotZeroRequested) {
    Solution sol;
    vector<int> flowerbed = {0};
    int n = 0;
    EXPECT_TRUE(sol.canPlaceFlowers(flowerbed, n));
}

// Test Case 6: Absolute minimum size (length = 1) - Filled plot, place 1
TEST(CanPlaceFlowersTest, SingleFilledPlotFailure) {
    Solution sol;
    vector<int> flowerbed = {1};
    int n = 1;
    EXPECT_FALSE(sol.canPlaceFlowers(flowerbed, n));
}

// Test Case 7: Planting at the very beginning (left edge case)
TEST(CanPlaceFlowersTest, PlantAtBeginning) {
    Solution sol;
    vector<int> flowerbed = {0, 0, 1};
    int n = 1;
    EXPECT_TRUE(sol.canPlaceFlowers(flowerbed, n));
}

// Test Case 8: Planting at the very end (right edge case)
TEST(CanPlaceFlowersTest, PlantAtEnd) {
    Solution sol;
    vector<int> flowerbed = {1, 0, 0};
    int n = 1;
    EXPECT_TRUE(sol.canPlaceFlowers(flowerbed, n));
}

// Test Case 9: All zeros flowerbed - Maximizing consecutive spots
TEST(CanPlaceFlowersTest, AllZerosMultipleFlowers) {
    Solution sol;
    vector<int> flowerbed = {0, 0, 0, 0, 0};
    int n = 3; // Can place at indices 0, 2, 4
    EXPECT_TRUE(sol.canPlaceFlowers(flowerbed, n));
}

// Test Case 10: All zeros flowerbed - Demanding more than theoretical maximum
TEST(CanPlaceFlowersTest, AllZerosExceedingMaximum) {
    Solution sol;
    vector<int> flowerbed = {0, 0, 0, 0, 0};
    int n = 4;
    EXPECT_FALSE(sol.canPlaceFlowers(flowerbed, n));
}

// Test Case 11: Alternating empty plots requiring careful traversal
TEST(CanPlaceFlowersTest, TightAlternatingPlots) {
    Solution sol;
    vector<int> flowerbed = {1, 0, 0, 0, 0, 0, 1};
    int n = 2; // Can place at indices 2 and 4
    EXPECT_TRUE(sol.canPlaceFlowers(flowerbed, n));
}