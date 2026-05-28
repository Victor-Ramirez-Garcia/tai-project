cmake_minimum_required(VERSION 3.10)
project(LeetCodeTestingSuite)

set(CMAKE_CXX_STANDARD 17)
find_package(GTest REQUIRED)
include(GoogleTest)

# 1. Gather all files
file(GLOB TEST_RUNNERS "test_unittest_*.cpp")

# 2. Process each test file individually
foreach(TEST_FILE ${TEST_RUNNERS})
    # Extract filename without path
    get_filename_component(TEST_NAME ${TEST_FILE} NAME_WE)
    
    # Extract ID specifically from the end of the string
    string(REGEX REPLACE "test_unittest_" "" TEST_ID ${TEST_NAME})
    
    # Define a unique target name based on the full test filename
    set(EXEC_NAME "run_${TEST_NAME}")
    
    # Find program files specific to this ID
    file(GLOB PROGRAM_SOURCES "program_${TEST_ID}_*.cpp")
    
    # Create the unique executable
    add_executable(${EXEC_NAME} ${TEST_FILE} ${PROGRAM_SOURCES})
    target_link_libraries(${EXEC_NAME} PRIVATE GTest::gtest_main)
    
    # Use gtest_discover_tests correctly
    gtest_discover_tests(${EXEC_NAME} 
        TEST_PREFIX "${TEST_ID}."
        DISCOVERY_MODE PRE_TEST
    )
endforeach()