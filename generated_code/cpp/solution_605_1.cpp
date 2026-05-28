#include <vector>

using namespace std;

class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // If no flowers need to be planted, it's always possible.
        if (n == 0) return true;
        
        int size = flowerbed.size();
        
        // Single-pass greedy approach to find empty plots.
        for (int i = 0; i < size; ++i) {
            // Check if the current plot is empty.
            if (flowerbed[i] == 0) {
                // Check if the left plot is empty or out of bounds.
                bool left_empty = (i == 0 || flowerbed[i - 1] == 0);
                // Check if the right plot is empty or out of bounds.
                bool right_empty = (i == size - 1 || flowerbed[i + 1] == 0);
                
                // If both sides are empty, we can plant a flower here.
                if (left_empty && right_empty) {
                    flowerbed[i] = 1; // Plant the flower
                    n--;             // Decrement the required flower count
                    
                    // Optimization: if all required flowers are planted, we can stop early.
                    if (n == 0) return true;
                }
            }
        }
        
        return n <= 0;
    }
};