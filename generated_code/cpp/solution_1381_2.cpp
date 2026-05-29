#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
private:
    int max_score = 0;

    // Backtracking function to explore all combinations of forming words
    void backtrack(int index, int current_score, vector<int>& letter_counts, 
                   const vector<string>& words, const vector<int>& score) {
        // Update the maximum score found so far
        max_score = max(max_score, current_score);

        // Base case: if we've processed all words, terminate the branch
        if (index == words.size()) {
            return;
        }

        // Option 1: Do not include words[index]
        backtrack(index + 1, current_score, letter_counts, words, score);

        // Option 2: Try to include words[index]
        bool can_form = true;
        int word_score = 0;
        vector<int> used_letters(26, 0);

        // Check if words[index] can be formed with the remaining letters
        for (char c : words[index]) {
            int idx = c - 'a';
            used_letters[idx]++;
            if (used_letters[idx] > letter_counts[idx]) {
                can_form = false;
                break;
            }
            word_score += score[idx];
        }

        // If it can be formed, deduct letters and recurse, then backtrack (restore letters)
        if (can_form) {
            for (int i = 0; i < 26; ++i) {
                letter_counts[i] -= used_letters[i];
            }

            backtrack(index + 1, current_score + word_score, letter_counts, words, score);

            for (int i = 0; i < 26; ++i) {
                letter_counts[i] += used_letters[i];
            }
        }
    }

public:
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        // Count the occurrences of each available letter
        vector<int> letter_counts(26, 0);
        for (char c : letters) {
            letter_counts[c - 'a']++;
        }

        max_score = 0;
        // Since words.length <= 14, an O(2^N) backtracking approach is highly optimal
        backtrack(0, 0, letter_counts, words, score);

        return max_score;
    }
};