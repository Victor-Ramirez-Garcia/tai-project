#include <vector>

using namespace std;

class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int n = nums.size();
        vector<int> result(n);
        
        // Count how many elements are strictly less than the pivot
        // and how many are strictly equal to the pivot.
        int less_count = 0;
        int equal_count = 0;
        for (int num : nums) {
            if (num < pivot) {
                less_count++;
            } else if (num == pivot) {
                equal_count++;
            }
        }
        
        // Determine the starting insertion indices for each category
        int less_ptr = 0;
        int equal_ptr = less_count;
        int greater_ptr = less_count + equal_count;
        
        // Iterate through the original array to populate the result array,
        // which naturally preserves the relative stable order of elements.
        for (int num : nums) {
            if (num < pivot) {
                result[less_ptr++] = num;
            } else if (num == pivot) {
                result[equal_ptr++] = num;
            } else {
                result[greater_ptr++] = num;
            }
        }
        
        return result;
    }
};