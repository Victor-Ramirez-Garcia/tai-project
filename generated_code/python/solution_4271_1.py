from typing import List

class Solution:
    def findDegrees(self, matrix: List[List[int]]) -> List[int]:
        """
        Calculates the degree of each vertex in an undirected graph 
        represented by a adjacency matrix.
        
        Time Complexity: O(n^2) where n is the number of vertices, 
                         as we iterate through every cell in the matrix.
        Space Complexity: O(1) auxiliary space (excluding the output array).
        """
        n = len(matrix)
        ans = [0] * n
        
        for i in range(n):
            # The degree of vertex i is the sum of 1s in its corresponding row.
            # In an undirected graph with no self-loops, this counts all incident edges.
            # If self-loops are possible, matrix[i][i] == 1 adds 1 to the degree.
            ans[i] = sum(matrix[i])
            
        return ans