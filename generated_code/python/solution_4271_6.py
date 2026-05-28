from typing import List

class Solution:
    def findDegrees(self, matrix: List[List[int]]) -> List[int]:
        # The degree of a vertex in an adjacency matrix representation of a graph
        # is simply the sum of elements in its corresponding row (excluding self-loops if matrix[i][i] == 1,
        # but standard adjacency matrices for simple graphs have 0 on the diagonal).
        # Time Complexity: O(n^2) to visit each cell in the matrix.
        # Space Complexity: O(n) to store the degrees of the n vertices.
        return [sum(row) for row in matrix]