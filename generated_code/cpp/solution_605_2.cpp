#include <vector>

using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // If no flowers need to be planted, it's always possible.
        if (n <= 0) return true;
        
        int size = flowerbed.size();
        
        // Single-pass Greedy approach: Traverse the flowerbed and place a flower 
        // whenever we find an empty plot with empty or non-existent neighbors.
        for (int i = 0; i < size; ++i) {
            if (flowerbed[i] == 0) {
                // Check if the left plot is empty or out of bounds
                bool left_empty = (i == 0 || flowerbed[i - 1] == 0);
                // Check if the right plot is empty or out of bounds
                bool right_empty = (i == size - 1 || flowerbed[i + 1] == 0);
                
                if (left_empty && right_empty) {
                    flowerbed[i] = 1; // Plant a flower
                    n--;              // Decrement the required number of flowers
                    
                    if (n == 0) return true; // Early exit if all flowers are planted
                }
            }
        }
        
        return n <= 0;
    }
};