#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        // Frequency array for the available letters
        vector<int> count(26, 0);
        for (char c : letters) {
            count[c - 'a']++;
        }
        
        // Since words.length <= 14, backtracking/DFS exploring all subsets is optimal.
        // Time Complexity: O(2^N * L), where N is number of words and L is max length of a word.
        // Space Complexity: O(N) for the recursion stack.
        return backtrack(0, words, count, score);
    }

private:
    int backtrack(int index, const vector<string>& words, vector<int>& count, const vector<int>& score) {
        if (index == words.size()) {
            return 0;
        }

        // Option 1: Skip the current word
        int max_score = backtrack(index + 1, words, count, score);

        // Option 2: Try to include the current word
        const string& word = words[index];
        bool can_form = true;
        int current_word_score = 0;
        
        // Form the word and check if we have enough letters
        for (char c : word) {
            int char_idx = c - 'a';
            count[char_idx]--;
            current_word_score += score[char_idx];
            if (count[char_idx] < 0) {
                can_form = false;
            }
        }

        // If the word can be successfully formed, explore further
        if (can_form) {
            max_score = max(max_score, current_word_score + backtrack(index + 1, words, count, score));
        }

        // Backtrack: restore the letter frequencies
        for (char c : word) {
            count[c - 'a']++;
        }

        return max_score;
    }
};