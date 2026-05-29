#include <vector>
#include <queue>
#include <tuple>

using namespace std;

class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        // Lambda to calculate the marginal gain in pass ratio if one student is added
        auto get_gain = [](double pass, double total) {
            return (pass + 1) / (total + 1) - pass / total;
        };

        // Max-heap stores elements as {gain, pass, total}
        // We want the class that gives the maximum gain at the top
        priority_queue<tuple<double, int, int>> max_heap;

        double total_ratio = 0.0;

        // Initialize the heap with the initial gain of each class
        for (const auto& c : classes) {
            int pass = c[0];
            int total = c[1];
            total_ratio += (double)pass / total;
            max_heap.push({get_gain(pass, total), pass, total});
        }

        // Greedily distribute each extra student to the class with the highest potential gain
        for (int i = 0; i < extraStudents; ++i) {
            auto [current_gain, pass, total] = max_heap.top();
            max_heap.pop();

            // Subtract the old ratio from our tracking sum and add the new one
            total_ratio += current_gain;

            // Increment the student counts for this class
            pass++;
            total++;

            // Push the updated class back into the heap with its new potential gain
            max_heap.push({get_gain(pass, total), pass, total});
        }

        // Return the average pass ratio across all classes
        return total_ratio / classes.size();
    }
};