cmake_minimum_required(VERSION 3.10)
project(LeetCodeTestingSuite)

set(CMAKE_CXX_STANDARD 17)

find_package(GTest REQUIRED)
include(GoogleTest)

# Find all test runner files
file(GLOB TEST_RUNNERS "test_unittest_*.cpp")

foreach(TEST_FILE ${TEST_RUNNERS})
    # Extract ID (e.g., 401)
    string(REGEX MATCH "[0-9]+" TEST_ID ${TEST_FILE})
    
    # 1. Get all program files for this ID
    file(GLOB PROGRAM_SOURCES "program_${TEST_ID}_*.cpp")
    
    # 2. Define the executable name
    set(EXEC_NAME "run_tests_${TEST_ID}")
    
    # 3. Only add the executable if it hasn't been created yet
    if(NOT TARGET ${EXEC_NAME})
        add_executable(${EXEC_NAME} ${TEST_FILE} ${PROGRAM_SOURCES})
        
        target_link_libraries(${EXEC_NAME} GTest::gtest_main)
        gtest_discover_tests(${EXEC_NAME})
    endif()
endforeach()