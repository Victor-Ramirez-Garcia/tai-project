#include <vector>
#include <string>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.length();
        vector<int> ans(n, 0);
        
        // This problem can be solved optimally in O(N) time and O(1) extra space
        // by accumulating operations from left-to-right and right-to-left.
        
        // Pass 1: Calculate operations needed to bring all balls from the left side of i to box i
        int left_balls = 0;
        int left_ops = 0;
        for (int i = 0; i < n; ++i) {
            ans[i] += left_ops;
            if (boxes[i] == '1') {
                left_balls++;
            }
            // As we move to the next box, every accumulated ball requires 1 extra operation
            left_ops += left_balls;
        }
        
        // Pass 2: Calculate operations needed to bring all balls from the right side of i to box i
        int right_balls = 0;
        int right_ops = 0;
        for (int i = n - 1; i >= 0; --i) {
            ans[i] += right_ops;
            if (boxes[i] == '1') {
                right_balls++;
            }
            // As we move to the previous box, every accumulated ball requires 1 extra operation
            right_ops += right_balls;
        }
        
        return ans;
    }
};