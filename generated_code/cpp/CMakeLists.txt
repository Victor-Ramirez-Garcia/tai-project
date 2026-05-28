cmake_minimum_required(VERSION 3.10)
project(LeetCodeTestingSuite)

set(CMAKE_CXX_STANDARD 17)
find_package(GTest REQUIRED)
include(GoogleTest)

# IMPORTANT: Ensure the compiler looks in the current directory for 
# the 'solution_proxy.h' file that your Python runner generates.
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

# 1. Gather all test runners
file(GLOB TEST_RUNNERS "test_unittest_*.cpp")

# 2. Process each test file individually
foreach(TEST_FILE ${TEST_RUNNERS})
    # Extract filename without path
    get_filename_component(TEST_NAME ${TEST_FILE} NAME_WE)
    
    # Extract ID specifically from the end of the string
    string(REGEX REPLACE "test_unittest_" "" TEST_ID ${TEST_NAME})
    
    # Define a unique target name
    set(EXEC_NAME "run_${TEST_NAME}")
    
    # We no longer glob PROGRAM_SOURCES. 
    # The test file includes "solution_proxy.h", which the runner updates.
    # Therefore, the test file itself is the only source needed for the executable.
    add_executable(${EXEC_NAME} ${TEST_FILE})
    
    target_link_libraries(${EXEC_NAME} PRIVATE GTest::gtest_main)
    
    # Use gtest_discover_tests
    gtest_discover_tests(${EXEC_NAME} 
        TEST_PREFIX "${TEST_ID}."
        DISCOVERY_MODE PRE_TEST
    )
endforeach()