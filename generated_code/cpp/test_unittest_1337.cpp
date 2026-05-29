#include <gtest/gtest.h>
#include "solution_proxy.h"

// Test fixture for Skiplist testing
class SkiplistTest : public ::testing::Test {
protected:
    Skiplist skiplist;
};

// Tests the exact sequence given in the problem description example
TEST_F(SkiplistTest, ExampleScenario) {
    skiplist.add(1);
    skiplist.add(2);
    skiplist.add(3);
    EXPECT_FALSE(skiplist.search(0));
    skiplist.add(4);
    EXPECT_TRUE(skiplist.search(1));
    EXPECT_FALSE(skiplist.erase(0));
    EXPECT_TRUE(skiplist.erase(1));
    EXPECT_FALSE(skiplist.search(1));
}

// Tests searching and erasing on an empty Skiplist
TEST_F(SkiplistTest, EmptySkiplist) {
    EXPECT_FALSE(skiplist.search(10));
    EXPECT_FALSE(skiplist.erase(10));
}

// Tests handling of duplicate values within the Skiplist
TEST_F(SkiplistTest, DuplicateValues) {
    skiplist.add(5);
    skiplist.add(5);
    skiplist.add(5);
    
    // Search should find the duplicates
    EXPECT_TRUE(skiplist.search(5));
    
    // Erase should remove one instance at a time
    EXPECT_TRUE(skiplist.erase(5));
    EXPECT_TRUE(skiplist.search(5));
    
    EXPECT_TRUE(skiplist.erase(5));
    EXPECT_TRUE(skiplist.search(5));
    
    EXPECT_TRUE(skiplist.erase(5));
    EXPECT_FALSE(skiplist.search(5));
    EXPECT_FALSE(skiplist.erase(5));
}

// Tests edge case values (minimum, maximum, and zero values)
TEST_F(SkiplistTest, ExtremeValues) {
    int min_val = 0;
    int max_val = 20000;

    skiplist.add(min_val);
    skiplist.add(max_val);

    EXPECT_TRUE(skiplist.search(min_val));
    EXPECT_TRUE(skiplist.search(max_val));

    EXPECT_TRUE(skiplist.erase(min_val));
    EXPECT_FALSE(skiplist.search(min_val));

    EXPECT_TRUE(skiplist.erase(max_val));
    EXPECT_FALSE(skiplist.search(max_val));
}

// Tests order preservation and lookups across sequential additions
TEST_F(SkiplistTest, SequentialInsertionsAndDeletions) {
    for (int i = 1; i <= 50; ++i) {
        skiplist.add(i);
    }

    for (int i = 1; i <= 50; ++i) {
        EXPECT_TRUE(skiplist.search(i));
    }

    // Verify values outside the range do not exist
    EXPECT_FALSE(skiplist.search(0));
    EXPECT_FALSE(skiplist.search(51));

    // Remove even numbers
    for (int i = 2; i <= 50; i += 2) {
        EXPECT_TRUE(skiplist.erase(i));
    }

    // Verify odd numbers remain and even numbers are gone
    for (int i = 1; i <= 50; ++i) {
        if (i % 2 == 1) {
            EXPECT_TRUE(skiplist.search(i));
        } else {
            EXPECT_FALSE(skiplist.search(i));
        }
    }
}