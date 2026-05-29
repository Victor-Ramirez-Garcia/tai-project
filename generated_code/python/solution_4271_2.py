from typing import List

class Solution:
    def findDegrees(self, matrix: List[List[int]]) -> List[int]:
        """
        Calculates the degree of each vertex in an undirected graph.
        
        Algorithm:
        The degree of a vertex i in an adjacency matrix is simply the sum of 
        the elements in its corresponding row (matrix[i]), since matrix[i][j] = 1 
        indicates an edge and matrix[i][j] = 0 indicates no edge.
        
        Time Complexity: O(n^2) where n is the number of vertices, as we visit each cell once.
        Space Complexity: O(1) auxiliary space (excluding the output array).
        """
        # Sum each row to get the degree of each vertex
        return [sum(row) for row in matrix]