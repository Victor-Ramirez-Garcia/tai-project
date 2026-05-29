#include <vector>
#include <string>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.length();
        vector<int> answer(n, 0);
        
        // This problem can be optimized to O(n) time using a prefix/suffix accumulation strategy.
        // Instead of calculating the distance from every ball to every box independently (O(n^2)),
        // we can track the accumulated operations dynamically by iterating from left to right, 
        // and then from right to left.
        
        // Pass 1: Left-to-Right
        // Calculate operations needed to bring all balls to the left of index i to index i.
        int count = 0; // Number of balls seen so far from the left
        int ops = 0;   // Accumulation of operations to bring those balls to the current index
        for (int i = 0; i < n; ++i) {
            answer[i] += ops;
            if (boxes[i] == '1') {
                count++;
            }
            ops += count; // Each ball seen so far takes 1 more step to get to the next index
        }
        
        // Pass 2: Right-to-Left
        // Calculate operations needed to bring all balls to the right of index i to index i.
        count = 0; // Reset number of balls seen so far from the right
        ops = 0;   // Reset accumulation of operations
        for (int i = n - 1; i >= 0; --i) {
            answer[i] += ops;
            if (boxes[i] == '1') {
                count++;
            }
            ops += count; // Each ball seen so far takes 1 more step to get to the next index (moving left)
        }
        
        // Time Complexity: O(n) - Two linear passes over the string.
        // Space Complexity: O(1) auxiliary space (excluding the output vector).
        return answer;
    }
};