import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Helper function to calculate the gain in pass ratio if one student is added
        def get_gain(p: int, t: int) -> float:
            return (p + 1) / (t + 1) - p / t

        # Max-heap to always pick the class that benefits the most from an extra student.
        # Python's heapq is a min-heap by default, so we store negative gain to simulate a max-heap.
        max_heap = []
        for p, t in classes:
            gain = get_gain(p, t)
            max_heap.append((-gain, p, t))
        
        heapq.heapify(max_heap)

        # Greedily allocate each extra student to the class with the maximum ratio gain
        for _ in range(extraStudents):
            neg_gain, p, t = heapq.heappop(max_heap)
            p += 1
            t += 1
            new_gain = get_gain(p, t)
            heapq.heappush(max_heap, (-new_gain, p, t))

        # Calculate the final total pass ratio across all classes
        total_ratio = 0.0
        for _, p, t in max_heap:
            total_ratio += p / t

        return total_ratio / len(classes)