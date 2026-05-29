#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        
        // Iterate through each operation in the list.
        // Time Complexity: O(N) where N is the number of operations.
        // Space Complexity: O(1) auxiliary space.
        for (const string& op : operations) {
            // Checking the middle character (index 1) is sufficient to distinguish 
            // between increment ('+') and decrement ('-') operations.
            if (op[1] == '+') {
                x++;
            } else {
                x--;
            }
        }
        
        return x;
    }
};