#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        // Lambda to calculate the potential gain in pass ratio if we add 1 student to a class
        auto getGain = [](double pass, double total) {
            return ((pass + 1.0) / (total + 1.0)) - (pass / total);
        };

        // Max-heap stores elements as {gain, {pass, total}}
        // We sort by the gain in descending order to always pick the class with the maximum impact
        priority_queue<pair<double, pair<int, int>>> maxHeap;

        // Populate the heap with the initial classes and their potential gains
        for (const auto& c : classes) {
            double gain = getGain(c[0], c[1]);
            maxHeap.push({gain, {c[0], c[1]}});
        }

        // Greedy approach: assign each extra student one by one to the class yielding the highest gain
        while (extraStudents > 0) {
            auto [currentGain, studentCounts] = maxHeap.top();
            maxHeap.pop();

            int pass = studentCounts.first;
            int total = studentCounts.second;

            // Increment the student counts for the chosen class
            pass++;
            total++;
            extraStudents--;

            // Recalculate the next potential gain and push back into the heap
            maxHeap.push({getGain(pass, total), {pass, total}});
        }

        // Calculate the final total pass ratio across all classes
        double totalPassRatio = 0.0;
        while (!maxHeap.empty()) {
            auto [_, studentCounts] = maxHeap.top();
            maxHeap.pop();
            totalPassRatio += (double)studentCounts.first / studentCounts.second;
        }

        // Return the average pass ratio
        return totalPassRatio / classes.size();
    }
};