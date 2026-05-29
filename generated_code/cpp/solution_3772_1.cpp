#include <vector>
#include <algorithm>
#include <set>
#include <numeric>

using namespace std;

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        int ans = 0;
        int inversionsCount = 0;

        // Doubly linked list tracking for current active elements
        vector<int> nextIndices(n);
        vector<int> prevIndices(n);
        vector<long long> values(nums.begin(), nums.end());

        for (int i = 0; i < n; ++i) {
            nextIndices[i] = i + 1;
            prevIndices[i] = i - 1;
        }

        // Custom comparator for the set to ensure we pick the minimum sum pair.
        // If sums are equal, we break ties by selecting the leftmost pair (smaller index).
        auto comp = [&](const pair<long long, int>& a, const pair<long long, int>& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second < b.second;
        };
        set<pair<long long, int>, decltype(comp)> pairSums(comp);

        // Populate initial adjacent pair sums and inversion counts
        for (int i = 0; i < n - 1; ++i) {
            pairSums.insert({values[i] + values[i + 1], i});
            if (values[i + 1] < values[i]) {
                ++inversionsCount;
            }
        }

        // Loop dynamically merges pairs as long as the array is not fully non-decreasing
        while (inversionsCount > 0) {
            ++ans;
            
            auto smallestPair = *pairSums.begin();
            pairSums.erase(pairSums.begin());

            long long pairSum = smallestPair.first;
            int currIndex = smallestPair.second;

            int nextIndex = nextIndices[currIndex];
            int prevIndex = prevIndices[currIndex];

            // Re-evaluate inversion changes around the current left element before it absorbs nextIndex
            if (prevIndex >= 0) {
                long long oldPairSum = values[prevIndex] + values[currIndex];
                long long newPairSum = values[prevIndex] + pairSum;
                pairSums.erase({oldPairSum, prevIndex});
                pairSums.insert({newPairSum, prevIndex});

                if (values[prevIndex] > values[currIndex]) --inversionsCount;
                if (values[prevIndex] > pairSum) ++inversionsCount;
            }

            if (values[nextIndex] < values[currIndex]) --inversionsCount;

            // Re-evaluate inversion changes around the element next to nextIndex
            int nextNextIndex = (nextIndex < n) ? nextIndices[nextIndex] : n;
            if (nextNextIndex < n) {
                long long oldPairSum = values[nextIndex] + values[nextNextIndex];
                long long newPairSum = pairSum + values[nextNextIndex];
                pairSums.erase({oldPairSum, nextIndex});
                pairSums.insert({newPairSum, currIndex});

                if (values[nextNextIndex] < values[nextIndex]) --inversionsCount;
                if (values[nextNextIndex] < pairSum) ++inversionsCount;
                
                prevIndices[nextNextIndex] = currIndex;
            }

            // Perform the logical merge in the doubly linked list structures
            nextIndices[currIndex] = nextNextIndex;
            values[currIndex] = pairSum;
        }

        return ans;
    }
};