import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        To maximize the average pass ratio, we need to maximize the sum of pass ratios.
        This is a greedy problem where we want to allocate each extra student to the class
        that yields the highest *incremental gain* in its pass ratio.
        
        The incremental gain for a class with (pass, total) is:
        gain = ((pass + 1) / (total + 1)) - (pass / total)
        
        We can use a max-heap to efficiently fetch and update the class with the highest gain.
        Since Python's heapq is a min-heap, we push negative gains.
        
        Time Complexity: O(N log N + K log N), where N = len(classes) and K = extraStudents.
        Space Complexity: O(N) to store the elements in the heap.
        """
        
        # Helper function to calculate the gain of adding one passing student
        def get_gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        # Initialize the max-heap with (-gain, pass, total)
        # We store negative gain because heapq is a min-heap by default
        max_heap = []
        for p, t in classes:
            gain = get_gain(p, t)
            max_heap.append((-gain, p, t))
            
        heapq.heapify(max_heap)

        # Greedily allocate each extra student to the class with the maximum gain
        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(max_heap)
            p += 1
            t += 1
            # Recalculate the gain for the updated class and push it back
            new_gain = get_gain(p, t)
            heapq.heappush(max_heap, (-new_gain, p, t))

        # Calculate the final average pass ratio
        total_ratio_sum = 0.0
        for _, p, t in max_heap:
            total_ratio_sum += p / t
            
        return total_ratio_sum / len(classes)