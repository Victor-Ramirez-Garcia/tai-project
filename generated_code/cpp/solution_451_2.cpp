#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    string frequencySort(string s) {
        // Step 1: Count the frequency of each character.
        unordered_map<char, int> counts;
        for (char c : s) {
            counts[c]++;
        }
        
        // Step 2: Use bucket sort for an optimal O(N) time complexity.
        // The maximum frequency a character can have is s.length().
        int n = s.length();
        vector<vector<char>> buckets(n + 1);
        for (auto& [ch, freq] : counts) {
            buckets[freq].push_back(ch);
        }
        
        // Step 3: Build the result string by iterating from the highest frequency bucket down to 1.
        string result;
        result.reserve(n); // Reserve memory to avoid reallocations.
        for (int freq = n; freq >= 1; --freq) {
            for (char ch : buckets[freq]) {
                result.append(freq, ch);
            }
        }
        
        return result;
    }
};