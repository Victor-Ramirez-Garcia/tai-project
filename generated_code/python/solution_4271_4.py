from typing import List

class Solution:
    def findDegrees(self, matrix: List[List[int]]) -> List[int]:
        """
        Calculates the degree of each vertex in an undirected graph.
        
        Algorithm:
        The degree of a vertex i in an adjacency matrix representation of an 
        undirected graph is equal to the sum of elements in its corresponding row 
        (or column), excluding any self-loops (if matrix[i][i] == 1). Assuming 
        no self-loops as per standard simple graph definitions, it is just the row sum.
        
        Time Complexity: O(n^2) where n is the number of vertices, as we visit each cell once.
        Space Complexity: O(n) to store the result array.
        """
        # The degree of vertex i is simply the sum of 1s in row i
        return [sum(row) for row in matrix]