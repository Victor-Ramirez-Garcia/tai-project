#include <gtest/gtest.h>
#include <vector>
#include <string>
#include <algorithm>
#include "solution_proxy.h"

using namespace std;

// Helper function to sort the outer and inner vectors to allow direct comparison.
void sortPaths(vector<vector<string>>& paths) {
    for (auto& path : paths) {
        // While the problem doesn't mandate internal component reordering, 
        // we ensure the overall structure is predictably sorted for comparison.
    }
    sort(paths.begin(), paths.end(), [](const vector<string>& a, const vector<string>& b) {
        return a < b;
    });
}

class DeleteDuplicateFolderTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Case 1: First example from the problem description
TEST_F(DeleteDuplicateFolderTest, Example1) {
    vector<vector<string>> paths = {{"a"}, {"c"}, {"d"}, {"a", "b"}, {"c", "b"}, {"d", "a"}};
    vector<vector<string>> expected = {{"d"}, {"d", "a"}};
    
    vector<vector<string>> result = solution.deleteDuplicateFolder(paths);
    
    sortPaths(result);
    sortPaths(expected);
    EXPECT_EQ(result, expected);
}

// Test Case 2: Second example from the problem description
TEST_F(DeleteDuplicateFolderTest, Example2) {
    vector<vector<string>> paths = {
        {"a"}, {"c"}, {"a", "b"}, {"c", "b"}, 
        {"a", "b", "x"}, {"a", "b", "x", "y"}, {"w"}, {"w", "y"}
    };
    vector<vector<string>> expected = {{"c"}, {"c", "b"}, {"a"}, {"a", "b"}};
    
    vector<vector<string>> result = solution.deleteDuplicateFolder(paths);
    
    sortPaths(result);
    sortPaths(expected);
    EXPECT_EQ(result, expected);
}

// Test Case 3: Third example from the problem description (No duplicates)
TEST_F(DeleteDuplicateFolderTest, Example3) {
    vector<vector<string>> paths = {{"a", "b"}, {"c", "d"}, {"c"}, {"a"}};
    vector<vector<string>> expected = {{"c"}, {"c", "d"}, {"a"}, {"a", "b"}};
    
    vector<vector<string>> result = solution.deleteDuplicateFolder(paths);
    
    sortPaths(result);
    sortPaths(expected);
    EXPECT_EQ(result, expected);
}

// Test Case 4: Minimal input constraints (Single root folder, no subfolders)
TEST_F(DeleteDuplicateFolderTest, MinimalInput) {
    vector<vector<string>> paths = {{"a"}};
    vector<vector<string>> expected = {{"a"}};
    
    vector<vector<string>> result = solution.deleteDuplicateFolder(paths);
    
    sortPaths(result);
    sortPaths(expected);
    EXPECT_EQ(result, expected);
}

// Test Case 5: Deeply nested structure where identical folders exist at different levels
TEST_F(DeleteDuplicateFolderTest, IdenticalStructuresAtDifferentLevels) {
    vector<vector<string>> paths = {
        {"a"}, {"a", "b"}, {"a", "b", "c"},
        {"x"}, {"x", "y"}, {"x", "y", "b"}, {"x", "y", "b", "c"}
    };
    // Structure under /a is (b -> c). Structure under /x/y is (b -> c).
    // Both /a and /x/y have the exact same subfolder structure, so they and their subfolders are deleted.
    // Remaining should be /x and /x/y (but wait, /x/y itself is marked, so it and its subfolders are gone).
    vector<vector<string>> expected = {{"x"}};
    
    vector<vector<string>> result = solution.deleteDuplicateFolder(paths);
    
    sortPaths(result);
    sortPaths(expected);
    EXPECT_EQ(result, expected);
}

// Test Case 6: Multiple empty folders at the root level should NOT be deleted 
// because folders are only identical if they contain the same non-empty set of subfolders.
TEST_F(DeleteDuplicateFolderTest, MultipleEmptyRootFolders) {
    vector<vector<string>> paths = {{"a"}, {"b"}, {"c"}};
    vector<vector<string>> expected = {{"a"}, {"b"}, {"c"}};
    
    vector<vector<string>> result = solution.deleteDuplicateFolder(paths);
    
    sortPaths(result);
    sortPaths(expected);
    EXPECT_EQ(result, expected);
}

// Test Case 7: Folders with different subfolder names (Not identical)
TEST_F(DeleteDuplicateFolderTest, DifferentSubfolderNames) {
    vector<vector<string>> paths = {{"a"}, {"a", "b"}, {"c"}, {"c", "d"}};
    vector<vector<string>> expected = {{"a"}, {"a", "b"}, {"c"}, {"c", "d"}};
    
    vector<vector<string>> result = solution.deleteDuplicateFolder(paths);
    
    sortPaths(result);
    sortPaths(expected);
    EXPECT_EQ(result, expected);
}