#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    string frequencySort(string s) {
        // Step 1: Count the frequency of each character.
        // Using an unordered_map to handle any potential character set, though constraints specify alphanumeric.
        unordered_map<char, int> freqMap;
        for (char c : s) {
            freqMap[c]++;
        }

        // Step 2: Use bucket sort for optimal O(N) time complexity.
        // Since the maximum frequency of any character cannot exceed the length of the string,
        // we create an array of strings (buckets) where the index represents the frequency.
        int n = s.length();
        vector<string> buckets(n + 1, "");
        for (auto& p : freqMap) {
            char c = p.first;
            int count = p.second;
            // Fill the bucket at index 'count' with 'count' repetitions of character 'c'
            buckets[count].append(count, c);
        }

        // Step 3: Accumulate the result from the highest frequency bucket down to the lowest.
        string result = "";
        for (int i = n; i > 0; --i) {
            if (!buckets[i].empty()) {
                result += buckets[i];
            }
        }

        return result;
    }
};