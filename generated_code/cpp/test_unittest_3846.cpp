#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

class MinOperationsTest : public ::testing::Test {
protected:
    Solution sol;
};

/**
 * @brief Example 1: Sum is close to a multiple of k.
 * nums = [1, 2, 3], k = 3. Sum = 6 (divisible by 3). Operations: 0.
 */
TEST_F(MinOperationsTest, Example1_AlreadyDivisible) {
    vector<int> nums = {1, 2, 3};
    int k = 3;
    EXPECT_EQ(sol.minOperations(nums, k), 0);
}

/**
 * @brief Example 2: Sum needs reduction.
 * nums = [3, 6, 9], k = 10. Sum = 18. Target = 10. Operations: 8.
 */
TEST_F(MinOperationsTest, Example2_ReductionNeeded) {
    vector<int> nums = {3, 6, 9};
    int k = 10;
    EXPECT_EQ(sol.minOperations(nums, k), 8);
}

/**
 * @brief Constraint: Minimum array size (1 element).
 * nums = [5], k = 3. Sum = 5. Target = 3. Operations: 2.
 */
TEST_F(MinOperationsTest, SingleElement) {
    vector<int> nums = {5};
    int k = 3;
    EXPECT_EQ(sol.minOperations(nums, k), 2);
}

/**
 * @brief Constraint: Array sum is less than k.
 * nums = [1, 1], k = 5. Sum = 2.
 * Since we can only decrement (replace nums[i] with nums[i] - 1), 
 * the only multiple of k reachable is 0. Operations: 2.
 */
TEST_F(MinOperationsTest, SumLessThanK) {
    vector<int> nums = {1, 1};
    int k = 5;
    EXPECT_EQ(sol.minOperations(nums, k), 2);
}

/**
 * @brief Case: Large k and large sum.
 * nums = {100, 100}, k = 7. Sum = 200. 200 % 7 = 4.
 * Operations required to reach 196 (multiple of 7): 4.
 */
TEST_F(MinOperationsTest, LargeValues) {
    vector<int> nums = {100, 100};
    int k = 7;
    EXPECT_EQ(sol.minOperations(nums, k), 4);
}

/**
 * @brief Case: All zeros.
 * Sum is 0, which is divisible by any k. Operations: 0.
 */
TEST_F(MinOperationsTest, AllZeros) {
    vector<int> nums = {0, 0, 0};
    int k = 4;
    EXPECT_EQ(sol.minOperations(nums, k), 0);
}

/**
 * @brief Case: k is 1.
 * Any integer is divisible by 1. Operations: 0.
 */
TEST_F(MinOperationsTest, KIsOne) {
    vector<int> nums = {1, 2, 3, 4, 5};
    int k = 1;
    EXPECT_EQ(sol.minOperations(nums, k), 0);
}