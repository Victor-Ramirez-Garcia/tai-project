#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

// Test Case 1: Standard Example 1 from the problem description
TEST(MaxAverageRatioTest, Example1) {
    Solution solution;
    vector<vector<int>> classes = {{1, 2}, {3, 5}, {2, 2}};
    int extraStudents = 2;
    double expected = 0.78333;
    double actual = solution.maxAverageRatio(classes, extraStudents);
    EXPECT_NEAR(actual, expected, 1e-5);
}

// Test Case 2: Standard Example 2 from the problem description
TEST(MaxAverageRatioTest, Example2) {
    Solution solution;
    vector<vector<int>> classes = {{2, 4}, {3, 9}, {4, 5}, {2, 10}};
    int extraStudents = 4;
    double expected = 0.53485;
    double actual = solution.maxAverageRatio(classes, extraStudents);
    EXPECT_NEAR(actual, expected, 1e-5);
}

// Test Case 3: Minimum constraints (1 class, 1 student in class, 1 extra student)
TEST(MaxAverageRatioTest, MinimumConstraints) {
    Solution solution;
    vector<vector<int>> classes = {{1, 1}};
    int extraStudents = 1;
    // (1+1)/(1+1) = 2/2 = 1.0
    double expected = 1.0;
    double actual = solution.maxAverageRatio(classes, extraStudents);
    EXPECT_NEAR(actual, expected, 1e-5);
}

// Test Case 4: Multiple classes where some already have 100% pass ratio
TEST(MaxAverageRatioTest, AlreadyFullPassRatio) {
    Solution solution;
    vector<vector<int>> classes = {{1, 2}, {3, 3}};
    int extraStudents = 1;
    // Adding to {1,2} gives {2,3} -> ratio 2/3. {3,3} is already 1.0. 
    // Avg = (2/3 + 1.0) / 2 = 1.666666 / 2 = 0.833333
    double expected = 0.833333;
    double actual = solution.maxAverageRatio(classes, extraStudents);
    EXPECT_NEAR(actual, expected, 1e-5);
}

// Test Case 5: Large number of extra students assigned to a single class
TEST(MaxAverageRatioTest, LargeExtraStudentsSingleClass) {
    Solution solution;
    vector<vector<int>> classes = {{1, 2}};
    int extraStudents = 99999;
    // Ratio becomes (1 + 99999) / (2 + 99999) = 100000 / 100001
    double expected = 100000.0 / 100001.0;
    double actual = solution.maxAverageRatio(classes, extraStudents);
    EXPECT_NEAR(actual, expected, 1e-5);
}

// Test Case 6: Classes with identical initial ratios but different total students
// The class with fewer total students gains more from an extra student.
// Gain for {1, 2} is (2/3 - 1/2) = 1/6 ~ 0.1666
// Gain for {2, 4} is (3/5 - 2/4) = 1/10 = 0.10
TEST(MaxAverageRatioTest, TieBreakingByPotentialGain) {
    Solution solution;
    vector<vector<int>> classes = {{1, 2}, {2, 4}};
    int extraStudents = 1;
    // Extra student should go to {1, 2} -> becomes {2, 3}
    // Avg = (2/3 + 2/4) / 2 = (0.666666 + 0.5) / 2 = 0.583333
    double expected = 0.583333;
    double actual = solution.maxAverageRatio(classes, extraStudents);
    EXPECT_NEAR(actual, expected, 1e-5);
}