#include <gtest/gtest.h>
#include "sol_0.cpp" // Replace with the actual filename containing foo()

// The TEST macro defines a test suite and the specific test name
TEST(FooTestSuite, ReturnsHelloWorld) {
    // Arrange: Define the expected output
    std::string expected = "Hello World!";
    
    // Act: Call the function
    std::string actual = foo();
    
    // Assert: Verify the result
    EXPECT_EQ(actual, expected);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}