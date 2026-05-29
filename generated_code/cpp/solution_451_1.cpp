#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    string frequencySort(string s) {
        // Step 1: Count the frequency of each character
        unordered_map<char, int> freqMap;
        for (char c : s) {
            freqMap[c]++;
        }

        // Step 2: Group characters by their frequency using Bucket Sort.
        // The maximum possible frequency is the length of the string `s`.
        int n = s.length();
        vector<vector<char>> buckets(n + 1);
        for (auto& p : freqMap) {
            buckets[p.second].push_back(p.first);
        }

        // Step 3: Build the result string by iterating from the highest bucket to the lowest.
        // Time Complexity: O(N) where N is the length of the string.
        // Space Complexity: O(N) to store frequencies and the bucket structures.
        string result;
        result.reserve(n); // Pre-allocate memory for efficiency
        
        for (int freq = n; freq >= 1; --freq) {
            for (char c : buckets[freq]) {
                result.append(freq, c);
            }
        }

        return result;
    }
};