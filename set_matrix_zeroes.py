######################################################################
# https://leetcode.cn/problems/set-matrix-zeroes/
######################################################################

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_position = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    zero_position.append([i, j])

        for position in zero_position:
            for i in range(0, len(matrix[0])):
                matrix[position[0]][i] = 0

            for i in range(0, len(matrix)):
                matrix[i][position[1]] = 0

if __name__ == "__main__":
    s = Solution()

    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix)
    print(matrix)

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(matrix)
    print(matrix)