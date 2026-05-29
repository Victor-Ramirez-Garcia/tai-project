from typing import List

class Solution:
    def findDegrees(self, matrix: List[List[int]]) -> List[int]:
        """
        Calculates the degree of each vertex in an undirected graph.
        
        Time Complexity: O(n^2) - We iterate through the entire n x n adjacency matrix.
        Space Complexity: O(1) auxiliary space (excluding the output array).
        """
        # Since it's an undirected graph represented by an adjacency matrix, 
        # the degree of vertex i is simply the sum of elements in the i-th row 
        # (excluding the self-loop matrix[i][i] if the problem definition or constraints 
        # imply matrix[i][i] can be 1, but standard definition sums the row).
        return [sum(row) for row in matrix]