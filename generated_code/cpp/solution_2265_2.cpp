#include <vector>

using namespace std;

/**
 * Algorithm: Two-Pass / Linear Scan with Pre-allocation
 * Time Complexity: O(n) - We traverse the array a constant number of times.
 * Space Complexity: O(n) - We need a result array to store the rearranged elements.
 * 
 * Logic:
 * To maintain the relative order (stability) and handle the three partitions 
 * (less than, equal to, greater than), we perform a three-pass approach or 
 * calculate the counts first. For optimal performance, we can pre-calculate 
 * the starting indices for each partition or simply use a single pass to fill 
 * the result array by checking conditions in sequence.
 */
class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        int n = nums.size();
        vector<int> result(n);
        
        int lessCount = 0;
        int pivotCount = 0;
        
        // First pass: Count elements less than pivot and equal to pivot
        // to determine the starting positions for each section in the result array.
        for (int num : nums) {
            if (num < pivot) {
                lessCount++;
            } else if (num == pivot) {
                pivotCount++;
            }
        }
        
        // Pointers for placing elements into their respective sections
        int left = 0;               // Start of 'less than' section
        int mid = lessCount;        // Start of 'equal' section
        int right = lessCount + pivotCount; // Start of 'greater than' section
        
        // Second pass: Populate the result array while maintaining relative order.
        // Because we iterate through 'nums' from left to right, we naturally 
        // preserve the original relative order within each partition.
        for (int num : nums) {
            if (num < pivot) {
                result[left++] = num;
            } else if (num == pivot) {
                result[mid++] = num;
            } else {
                result[right++] = num;
            }
        }
        
        return result;
    }
};