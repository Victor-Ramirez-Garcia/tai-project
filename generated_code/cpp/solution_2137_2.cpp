#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        
        for (const string& op : operations) {
            // Checking the middle character (index 1) is sufficient to distinguish 
            // between increment ('+') and decrement ('-') operations.
            // "++X" or "X++" will always have '+' at index 1.
            // "--X" or "X--" will always have '-' at index 1.
            if (op[1] == '+') {
                x++;
            } else {
                x--;
            }
        }
        
        return x;
    }
};