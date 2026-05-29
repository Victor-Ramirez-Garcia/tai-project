from typing import List
from sortedcontainers import SortedList

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        # Track the number of inversions (where nums[i] > nums[i+1])
        # The array is sorted / non-decreasing when inversionsCount == 0
        inversionsCount = sum(nums[i + 1] < nums[i] for i in range(n - 1))
        
        # Doubly linked list representations using indexing
        nextIndices = [i + 1 for i in range(n)]
        prevIndices = [i - 1 for i in range(n)]
        
        # Sorted list acting as a min-heap to keep track of adjacent pair sums.
        # Elements are stored as (pair_sum, left_index). Ties are naturally broken
        # by the leftmost index due to the tuple comparison format.
        pairSums = SortedList((nums[i] + nums[i + 1], i) for i in range(n - 1))
        
        while inversionsCount > 0:
            ans += 1
            # Retrieve and remove the leftmost pair with the minimum sum
            smallestPair = pairSums.pop(0)
            pairSum, currIndex = smallestPair
            
            nextIndex = nextIndices[currIndex]
            prevIndex = prevIndices[currIndex]
            
            # If a previous element exists, the relationship between prevIndex and currIndex changes
            if prevIndex >= 0:
                oldPairSum = nums[prevIndex] + nums[currIndex]
                newPairSum = nums[prevIndex] + pairSum
                pairSums.remove((oldPairSum, prevIndex))
                pairSums.add((newPairSum, prevIndex))
                
                # Update inversion status for (prevIndex, currIndex)
                if nums[prevIndex] > nums[currIndex]:
                    inversionsCount -= 1
                if nums[prevIndex] > pairSum:
                    inversionsCount += 1
                    
            # Update inversion status for the merged pair (currIndex, nextIndex) being removed
            if nums[nextIndex] < nums[currIndex]:
                inversionsCount -= 1
                
            nextNextIndex = nextIndices[nextIndex] if nextIndex < n else n
            
            # If an element exists after the merged pair, update its relationship with currIndex
            if nextNextIndex < n:
                oldPairSum = nums[nextIndex] + nums[nextNextIndex]
                newPairSum = pairSum + nums[nextNextIndex]
                pairSums.remove((oldPairSum, nextIndex))
                pairSums.add((newPairSum, currIndex))
                
                # Update inversion status for (nextIndex, nextNextIndex)
                if nums[nextNextIndex] < nums[nextIndex]:
                    inversionsCount -= 1
                if nums[nextNextIndex] < pairSum:
                    inversionsCount += 1
                    
                prevIndices[nextNextIndex] = currIndex
                
            # Finalize the removal of nextIndex and update the value of currIndex
            nextIndices[currIndex] = nextNextIndex
            nums[currIndex] = pairSum
            
        return ans