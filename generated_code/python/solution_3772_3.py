import collections
from typing import List, Optional, Deque

# Definition for a binary tree node (included for self-containment if needed)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for singly-linked list (included for self-containment if needed)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        """
        To make the array non-decreasing with the minimum number of merge operations, 
        we want to find a partitioning of the array into contiguous subarrays such that 
        the sum of each subarray is non-decreasing, and the number of subarrays is maximized.
        Maximizing the number of subarrays minimizes the number of operations (n - parts).
        
        We use a Dynamic Programming approach combined with a monotonic queue / greedy choice.
        Let dp[i] be the maximum number of groups we can split the prefix nums[0...i-1] into.
        To maximize the chance of extending the sequence, we also want the last group's sum 
        to be as small as possible. Let min_last[i] be the minimum sum of the last group 
        in an optimal partitioning of nums[0...i-1].
        
        We can optimize the O(N^2) transitions to O(N) using a prefix sum array and a 
        monotonic queue, because we look for the largest j < i such that:
        pref[i] - pref[j] >= min_last[j]  =>  pref[i] >= pref[j] + min_last[j]
        """
        n = len(nums)
        if n <= 1:
            return 0
            
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
            
        # dp[i] stores the max number of groups for prefix of length i
        dp = [0] * (n + 1)
        # min_last[i] stores the minimum sum of the last group for prefix of length i
        min_last = [0] * (n + 1)
        
        # Deque stores indices of the prefix array. 
        # We maintain it such that pref[j] + min_last[j] is strictly increasing.
        q: Deque[int] = collections.deque([0])
        
        for i in range(1, n + 1):
            # Find the largest j in the queue that satisfies the condition
            # pref[i] >= pref[j] + min_last[j]
            best_j = 0
            while q and pref[i] >= pref[q[0]] + min_last[q[0]]:
                best_j = q.popleft()
                
            # best_j is now the optimal split point for prefix i
            dp[i] = dp[best_j] + 1
            min_last[i] = pref[i] - pref[best_j]
            
            # Put best_j back as it could be useful for future elements
            q.appendleft(best_j)
            
            # Maintain the monotonic property of the queue.
            # We remove elements from the back if they have a larger or equal 
            # (pref[j] + min_last[j]) value, because a smaller value is always better 
            # and appears earlier (or at the same position but more optimal).
            while q and (pref[q[-1]] + min_last[q[-1]] >= pref[i] + min_last[i]):
                q.pop()
                
            q.append(i)
            
        # Total operations = total elements - maximum number of valid non-decreasing groups
        return n - dp[n]