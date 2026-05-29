#include <gtest/gtest.h>
#include <string>
#include <unordered_map>
#include <algorithm>
#include "solution_proxy.h"

// Helper function to validate if a returned string is correctly sorted by frequency.
// This is necessary because multiple outputs can be valid for the same input.
void VerifyFrequencySort(const std::string& input, const std::string& result) {
    ASSERT_EQ(input.length(), result.length()) << "Result length matches input length.";

    std::unordered_map<char, int> counts;
    for (char c : input) {
        counts[c]++;
    }

    // Verify that all identical characters are contiguous in the result
    for (size_t i = 1; i < result.length(); ++i) {
        if (result[i] != result[i - 1]) {
            // If the character changed, the previous character should not appear again later
            for (size_t j = i + 1; j < result.length(); ++j) {
                ASSERT_NE(result[j], result[i - 1]) 
                    << "Character '" << result[i - 1] << "' is not grouped together in result: " << result;
            }
        }
    }

    // Verify that the frequencies are in decreasing order
    int prev_frequency = INT_MAX;
    size_t i = 0;
    while (i < result.length()) {
        char current_char = result[i];
        int current_frequency = 0;
        
        while (i < result.length() && result[i] == current_char) {
            current_frequency++;
            i++;
        }

        ASSERT_EQ(current_frequency, counts[current_char]) 
            << "Character '" << current_char << "' frequency mismatch.";
        ASSERT_LE(current_frequency, prev_frequency) 
            << "Result is not sorted in decreasing order of frequency: " << result;
        
        prev_frequency = current_frequency;
    }
}

TEST(FrequencySortTest, Example1_Tree) {
    Solution solution;
    std::string input = "tree";
    std::string result = solution.frequencySort(input);
    VerifyFrequencySort(input, result);
}

TEST(FrequencySortTest, Example2_Cccaaa) {
    Solution solution;
    std::string input = "cccaaa";
    std::string result = solution.frequencySort(input);
    VerifyFrequencySort(input, result);
}

TEST(FrequencySortTest, Example3_Aabb) {
    Solution solution;
    std::string input = "Aabb";
    std::string result = solution.frequencySort(input);
    VerifyFrequencySort(input, result);
}

TEST(FrequencySortTest, MinimumLengthConstraint) {
    Solution solution;
    std::string input = "a";
    std::string result = solution.frequencySort(input);
    VerifyFrequencySort(input, result);
}

TEST(FrequencySortTest, AllSameCharacters) {
    Solution solution;
    std::string input = "vvvvvvvv";
    std::string result = solution.frequencySort(input);
    VerifyFrequencySort(input, result);
}

TEST(FrequencySortTest, AllDistinctCharacters) {
    Solution solution;
    std::string input = "abcdefg";
    std::string result = solution.frequencySort(input);
    VerifyFrequencySort(input, result);
}

TEST(FrequencySortTest, IncludesDigits) {
    Solution solution;
    std::string input = "222113";
    std::string result = solution.frequencySort(input);
    VerifyFrequencySort(input, result);
}

TEST(FrequencySortTest, MixedAlphanumericCaseSensitive) {
    Solution solution;
    std::string input = "m1m1M1RwbWw";
    std::string result = solution.frequencySort(input);
    VerifyFrequencySort(input, result);
}

TEST(FrequencySortTest, LargeInputMaximumConstraint) {
    Solution solution;
    // Construct a large string within constraints (5 * 10^5 max)
    // 100,000 'a's, 200,000 'b's, 50,000 'c's, 150,000 'd's = 500,000 total length
    std::string input = std::string(100000, 'a') + 
                        std::string(200000, 'b') + 
                        std::string(50000, 'c') + 
                        std::string(150000, 'd');
    
    std::string result = solution.frequencySort(input);
    VerifyFrequencySort(input, result);
}