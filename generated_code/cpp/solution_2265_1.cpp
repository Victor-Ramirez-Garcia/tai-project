#include <vector>

using namespace std;

class Solution {
public:
    // Time Complexity: O(N) where N is the number of elements in nums. 
    // We iterate through the array twice (or once with a two-pointer trick). Here, we use a 
    // single-pass stable partition approach with an auxiliary result vector for clarity and O(N) space.
    // Space Complexity: O(N) to store the rearranged elements in the result vector.
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int n = nums.size();
        vector<int> result(n);
        
        int left = 0;
        int right = n - 1;
        
        // Two-pointer approach to fill smaller elements from the left and 
        // larger elements from the right to maintain their respective relative order.
        for (int i = 0, j = n - 1; i < n; ++i, --j) {
            if (nums[i] < pivot) {
                result[left++] = nums[i];
            }
            if (nums[j] > pivot) {
                result[right--] = nums[j];
            }
        }
        
        // Fill the remaining spots between 'left' and 'right' with the pivot value.
        while (left <= right) {
            result[left++] = pivot;
        }
        
        return result;
    }
};