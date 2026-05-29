import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        To maximize the average pass ratio, we need to maximize the sum of individual pass ratios.
        This is a greedy problem where we should repeatedly add a student to the class that 
        yields the maximum increase (gain) in its pass ratio.
        
        The current pass ratio is: pass / total
        If we add one student, the new ratio is: (pass + 1) / (total + 1)
        The gain is: ((pass + 1) / (total + 1)) - (pass / total)
        
        We can use a Max-Heap (simulated with negative values in Python's min-heap) to 
        always extract the class that offers the highest potential gain.
        
        Time Complexity: O(N + K log N) where N is classes.length and K is extraStudents.
        Space Complexity: O(N) to store the heap elements.
        """
        
        # Helper function to calculate the gain of adding 1 passing student
        def get_gain(p: int, t: int) -> float:
            return ((p + 1) / (t + 1)) - (p / t)
        
        # Build the max-heap. Python's heapq is a min-heap, so we store negative gain.
        # Elements are stored as (-gain, passed, total)
        max_heap = []
        for p, t in classes:
            gain = get_gain(p, t)
            max_heap.append((-gain, p, t))
            
        heapq.heapify(max_heap)
        
        # Distribute extra students greedily
        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(max_heap)
            # Add one student to this class
            p += 1
            t += 1
            # Recalculate gain and push back into the heap
            new_gain = get_gain(p, t)
            heapq.heappush(max_heap, (-new_gain, p, t))
            
        # Calculate the final average pass ratio
        total_ratio_sum = sum(p / t for _, p, t in max_heap)
        return total_ratio_sum / len(classes)