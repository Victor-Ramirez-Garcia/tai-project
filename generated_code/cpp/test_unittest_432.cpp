#include <gtest/gtest.h>
#include <string>
#include <vector>
#include "solution_proxy.h"

// Test Case covering the standard LeetCode example scenario
TEST(AllOneTest, ExampleCase) {
    AllOne allOne;
    allOne.inc("hello");
    allOne.inc("hello");
    EXPECT_EQ(allOne.getMaxKey(), "hello");
    EXPECT_EQ(allOne.getMinKey(), "hello");
    allOne.inc("leet");
    EXPECT_EQ(allOne.getMaxKey(), "hello");
    EXPECT_EQ(allOne.getMinKey(), "leet");
}

// Test Case evaluating behavior when the data structure is empty
TEST(AllOneTest, EmptyStructureReturnsEmptyStrings) {
    AllOne allOne;
    EXPECT_EQ(allOne.getMaxKey(), "");
    EXPECT_EQ(allOne.getMinKey(), "");
}

// Test Case covering element removal when its count drops to 0
TEST(AllOneTest, ElementRemovedWhenCountDropsToZero) {
    AllOne allOne;
    allOne.inc("key1");
    EXPECT_EQ(allOne.getMaxKey(), "key1");
    EXPECT_EQ(allOne.getMinKey(), "key1");
    
    allOne.dec("key1");
    EXPECT_EQ(allOne.getMaxKey(), "");
    EXPECT_EQ(allOne.getMinKey(), "");
}

// Test Case verifying that keys change max/min roles dynamically as counts change
TEST(AllOneTest, DynamicMaxMinUpdates) {
    AllOne allOne;
    allOne.inc("A");
    allOne.inc("B");
    allOne.inc("B");
    
    // "B" has count 2, "A" has count 1
    EXPECT_EQ(allOne.getMaxKey(), "B");
    EXPECT_EQ(allOne.getMinKey(), "A");
    
    allOne.inc("A");
    allOne.inc("A");
    
    // "A" has count 3, "B" has count 2
    EXPECT_EQ(allOne.getMaxKey(), "A");
    EXPECT_EQ(allOne.getMinKey(), "B");
}

// Test Case for when multiple keys share the same maximum or minimum counts
TEST(AllOneTest, MultipleKeysWithSameCount) {
    AllOne allOne;
    allOne.inc("key1");
    allOne.inc("key2");
    
    std::string maxKey = allOne.getMaxKey();
    std::string minKey = allOne.getMinKey();
    
    // Both keys have count 1, so both max and min keys should be either "key1" or "key2"
    EXPECT_TRUE(maxKey == "key1" || maxKey == "key2");
    EXPECT_TRUE(minKey == "key1" || minKey == "key2");
}

// Test Case with complex interleaved increments and decrements
TEST(AllOneTest, InterleavedIncrementsAndDecrements) {
    AllOne allOne;
    allOne.inc("apple");
    allOne.inc("banana");
    allOne.inc("apple");
    allOne.dec("banana"); 
    // apple: 2, banana: 0 (removed)
    
    EXPECT_EQ(allOne.getMaxKey(), "apple");
    EXPECT_EQ(allOne.getMinKey(), "apple");
    
    allOne.inc("cherry");
    allOne.inc("cherry");
    allOne.inc("cherry");
    // apple: 2, cherry: 3
    
    EXPECT_EQ(allOne.getMaxKey(), "cherry");
    EXPECT_EQ(allOne.getMinKey(), "apple");
    
    allOne.dec("cherry");
    allOne.dec("cherry");
    // apple: 2, cherry: 1
    
    EXPECT_EQ(allOne.getMaxKey(), "apple");
    EXPECT_EQ(allOne.getMinKey(), "cherry");
}