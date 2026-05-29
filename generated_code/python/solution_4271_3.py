from typing import List

class Solution:
    def findDegrees(self, matrix: List[List[int]]) -> List[int]:
        # The degree of a vertex in an adjacency matrix is simply the sum of its row 
        # (excluding self-loops, though standard simple graphs usually have 0 on the diagonal).
        # Time Complexity: O(n^2) where n is the number of vertices.
        # Space Complexity: O(1) auxiliary space (excluding the output array).
        return [sum(row) for row in matrix]