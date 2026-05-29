#include <gtest/gtest.h>
#include "solution_proxy.h"

// Test Case 1: Covering the example provided in the problem statement
TEST(MyLinkedListTest, ExampleScenario) {
    MyLinkedList* myLinkedList = new MyLinkedList();
    
    myLinkedList->addAtHead(1);
    myLinkedList->addAtTail(3);
    myLinkedList->addAtIndex(1, 2);    // Linked list becomes: 1 -> 2 -> 3
    
    EXPECT_EQ(myLinkedList->get(1), 2); // Returns 2
    
    myLinkedList->deleteAtIndex(1);    // Linked list becomes: 1 -> 3
    
    EXPECT_EQ(myLinkedList->get(1), 3); // Returns 3
    
    delete myLinkedList;
}

// Test Case 2: Testing edge cases with an empty linked list
TEST(MyLinkedListTest, EmptyListOperations) {
    MyLinkedList* myLinkedList = new MyLinkedList();
    
    // Index out of bounds on an empty list
    EXPECT_EQ(myLinkedList->get(0), -1);
    EXPECT_EQ(myLinkedList->get(5), -1);
    EXPECT_EQ(myLinkedList->get(-1), -1);
    
    // Deleting from an empty list should not crash or modify state improperly
    myLinkedList->deleteAtIndex(0);
    myLinkedList->deleteAtIndex(1);
    EXPECT_EQ(myLinkedList->get(0), -1);
    
    delete myLinkedList;
}

// Test Case 3: Testing index validation boundary conditions for addAtIndex
TEST(MyLinkedListTest, AddAtIndexBoundaries) {
    MyLinkedList* myLinkedList = new MyLinkedList();
    
    // Index greater than length should not insert
    myLinkedList->addAtIndex(1, 100);
    EXPECT_EQ(myLinkedList->get(0), -1);
    
    // Index equal to length should append at tail
    myLinkedList->addAtIndex(0, 10); // List: 10
    EXPECT_EQ(myLinkedList->get(0), 10);
    
    myLinkedList->addAtIndex(1, 20); // List: 10 -> 20
    EXPECT_EQ(myLinkedList->get(1), 20);
    
    // Negative index handling (should not insert or be treated as invalid)
    myLinkedList->addAtIndex(-1, 5);
    EXPECT_EQ(myLinkedList->get(0), 10);
    
    delete myLinkedList;
}

// Test Case 4: Testing deleteAtIndex boundary conditions
TEST(MyLinkedListTest, DeleteAtIndexBoundaries) {
    MyLinkedList* myLinkedList = new MyLinkedList();
    
    myLinkedList->addAtHead(3);
    myLinkedList->addAtHead(2);
    myLinkedList->addAtHead(1); // List: 1 -> 2 -> 3
    
    // Delete index out of bounds (equal to length)
    myLinkedList->deleteAtIndex(3);
    EXPECT_EQ(myLinkedList->get(2), 3);
    
    // Delete index out of bounds (greater than length)
    myLinkedList->deleteAtIndex(5);
    EXPECT_EQ(myLinkedList->get(2), 3);
    
    // Delete negative index
    myLinkedList->deleteAtIndex(-1);
    EXPECT_EQ(myLinkedList->get(0), 1);
    
    // Delete head node
    myLinkedList->deleteAtIndex(0); // List: 2 -> 3
    EXPECT_EQ(myLinkedList->get(0), 2);
    
    // Delete tail node
    myLinkedList->deleteAtIndex(1); // List: 2
    EXPECT_EQ(myLinkedList->get(0), 2);
    EXPECT_EQ(myLinkedList->get(1), -1);
    
    // Delete last remaining node
    myLinkedList->deleteAtIndex(0); // List: empty
    EXPECT_EQ(myLinkedList->get(0), -1);
    
    delete myLinkedList;
}

// Test Case 5: Testing multiple insertions at head and tail exclusively
TEST(MyLinkedListTest, HeadAndTailInsertions) {
    MyLinkedList* myLinkedList = new MyLinkedList();
    
    // Consecutive insertions at head
    myLinkedList->addAtHead(10);
    myLinkedList->addAtHead(20);
    myLinkedList->addAtHead(30); // List: 30 -> 20 -> 10
    
    EXPECT_EQ(myLinkedList->get(0), 30);
    EXPECT_EQ(myLinkedList->get(1), 20);
    EXPECT_EQ(myLinkedList->get(2), 10);
    
    // Consecutive insertions at tail
    myLinkedList->addAtTail(40);
    myLinkedList->addAtTail(50); // List: 30 -> 20 -> 10 -> 40 -> 50
    
    EXPECT_EQ(myLinkedList->get(3), 40);
    EXPECT_EQ(myLinkedList->get(4), 50);
    EXPECT_EQ(myLinkedList->get(5), -1);
    
    delete myLinkedList;
}