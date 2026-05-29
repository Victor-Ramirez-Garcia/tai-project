import heapq
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
            
        # Doubly-linked list arrays to track adjacent valid elements efficiently
        nxt = list(range(1, n + 1))
        prv = list(range(-1, n))
        
        # Track the active version/timestamp of pairs to avoid stale heap elements
        # version[i] is incremented whenever the right neighbor or value of element i changes
        version = [0] * n
        
        # Min-heap elements: (pair_sum, left_index, version_of_left_index)
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i, 0))
            
        # Count how many adjacent pairs are currently strictly decreasing (violating sorted order)
        # cnt_decreasing tracks the number of adjacent active pairs where nums[i] > nums[nxt[i]]
        cnt_decreasing = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                cnt_decreasing += 1
                
        ans = 0
        
        # Efficient Simulation using Heap and Doubly Linked List: O(N log N) Time
        while cnt_decreasing > 0:
            # Extract the global leftmost minimum-sum pair from the heap
            pair_sum, i, v = heapq.heappop(heap)
            
            # Lazy deletion check: if the version matches, this pair is still valid and adjacent
            if v != version[i] or nxt[i] >= n:
                continue
                
            j = nxt[i] # Right element of the selected pair
            
            # 1. Update the decreasing count by removing the old adjacencies that will be modified
            if nums[i] > nums[j]:
                cnt_decreasing -= 1
            if prv[i] != -1 and nums[prv[i]] > nums[i]:
                cnt_decreasing -= 1
            if nxt[j] != n and nums[j] > nums[nxt[j]]:
                cnt_decreasing -= 1
                
            # 2. Perform the operation: merge j into i
            nums[i] += nums[j]
            
            # 3. Update doubly-linked list structures to remove j
            nxt[i] = nxt[j]
            if nxt[j] != n:
                prv[nxt[j]] = i
                
            # 4. Invalidate old pairs involving elements that just changed
            version[i] += 1
            if prv[i] != -1:
                version[prv[i]] += 1
                
            # 5. Add back the newly formed adjacent pairs to the decreasing count