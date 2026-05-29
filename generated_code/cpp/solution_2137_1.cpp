#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;
        for (const string& op : operations) {
            // In all increment operations ("++X", "X++"), the character at index 1 is '+'
            // In all decrement operations ("--X", "X--"), the character at index 1 is '-'
            if (op[1] == '+') {
                x++;
            } else {
                x--;
            }
        }
        return x;
    }
};