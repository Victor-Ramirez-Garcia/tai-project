#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
private:
    // Helper function to calculate the marginal gain in pass ratio 
    // if we add one passing student to a class.
    double getGain(double pass, double total) {
        return (pass + 1) / (total + 1) - pass / total;
    }

public:
    double maxAverageRatio(vector<vector<int>>& classes, int extraStudents) {
        // Max-heap stores pairs of {gain, class_index} to always pick the 
        // class that yields the highest increase in pass ratio.
        priority_queue<pair<double, int>> maxHeap;
        
        // Initialize the heap with the potential gain for each class
        for (int i = 0; i < classes.size(); ++i) {
            double gain = getGain(classes[i][0], classes[i][1]);
            maxHeap.push({gain, i});
        }
        
        // Greedily distribute the extra students
        while (extraStudents > 0) {
            auto [currentGain, idx] = maxHeap.top();
            maxHeap.pop();
            
            // Add a student to the class that gives the maximum current gain
            classes[idx][0]++;
            classes[idx][1]++;
            extraStudents--;
            
            // Recalculate the gain for this class and push back into the heap
            double nextGain = getGain(classes[idx][0], classes[idx][1]);
            maxHeap.push({nextGain, idx});
        }
        
        // Calculate the final total sum of all pass ratios
        double totalRatioSum = 0.0;
        for (const auto& singleClass : classes) {
            totalRatioSum += (double)singleClass[0] / singleClass[1];
        }
        
        // The average pass ratio is the sum divided by the number of classes
        return totalRatioSum / classes.size();
    }
};