#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
private:
    int max_score = 0;

    // Backtracking function to explore all subsets of words
    void backtrack(int index, const vector<string>& words, vector<int>& letter_counts, const vector<int>& score, int current_score) {
        // Update the maximum score found so far
        max_score = max(max_score, current_score);

        // If all words have been considered, terminate the branch
        if (index == words.size()) {
            return;
        }

        // Option 1: Skip the current word
        backtrack(index + 1, words, letter_counts, score, current_score);

        // Option 2: Try to include the current word
        const string& word = words[index];
        bool can_form = true;
        int word_score = 0;
        
        // Track how many characters we borrow from letter_counts to form this word
        vector<int> used_counts(26, 0);

        for (char c : word) {
            int idx = c - 'a';
            used_counts[idx]++;
            if (used_counts[idx] > letter_counts[idx]) {
                can_form = false;
                break;
            }
            word_score += score[idx];
        }

        // If the word can be validly formed with remaining letters, proceed recursively
        if (can_form) {
            // Deduct the characters used by the current word
            for (int i = 0; i < 26; ++i) {
                letter_counts[i] -= used_counts[i];
            }

            // Recurse to the next word with the updated score and letter pool
            backtrack(index + 1, words, letter_counts, score, current_score + word_score);

            // Backtrack: Restore the character pool for other search branches
            for (int i = 0; i < 26; ++i) {
                letter_counts[i] += used_counts[i];
            }
        }
    }

public:
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        max_score = 0;
        
        // Count the frequencies of available characters in the pool
        vector<int> letter_counts(26, 0);
        for (char c : letters) {
            letter_counts[c - 'a']++;
        }

        // Since words.length <= 14, an O(2^N) backtracking approach is highly efficient and optimal
        backtrack(0, words, letter_counts, score, 0);

        return max_score;
    }
};