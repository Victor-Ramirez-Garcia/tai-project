#include <vector>
#include <string>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.length();
        vector<int> answer(n, 0);
        
        // This problem can be optimized to O(n) time complexity by using a two-pass approach.
        // We can compute the operations needed from the left side and the right side independently.
        
        // First pass: Left to Right
        // Track the number of balls seen so far from the left, and the cumulative operations.
        int left_balls = 0;
        int left_ops = 0;
        for (int i = 0; i < n; ++i) {
            answer[i] += left_ops;
            if (boxes[i] == '1') {
                left_balls++;
            }
            // Moving to the next box increases the total cost by the number of balls carried
            left_ops += left_balls;
        }
        
        // Second pass: Right to Left
        // Track the number of balls seen so far from the right, and the cumulative operations.
        int right_balls = 0;
        int right_ops = 0;
        for (int i = n - 1; i >= 0; --i) {
            answer[i] += right_ops;
            if (boxes[i] == '1') {
                right_balls++;
            }
            // Moving to the next box leftwards increases the total cost by the number of balls carried
            right_ops += right_balls;
        }
        
        return answer;
    }
};