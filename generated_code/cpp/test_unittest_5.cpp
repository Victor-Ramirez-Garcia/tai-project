#include <gtest/gtest.h>
#include "solution_5_1.cpp" // Replace with the actual filename containing foo()

// The TEST macro defines a test suite and the specific test name
TEST(FooTestSuite, ReturnsHelloWorld) {

    Solution solution; // Create an instance of the Solution class to call foo()
    // Arrange: Define the expected output
    std::string expected = "Hello World!";
    
    // Act: Call the function
    std::string actual = solution.foo();
    
    // Assert: Verify the result
    EXPECT_EQ(actual, expected);
}