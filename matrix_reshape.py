######################################################################
# https://leetcode.cn/problems/reshape-the-matrix/
######################################################################

from typing import List
import numpy as np

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        try:
            mat_array = np.array(mat)
            result_array = mat_array.reshape(r, c)
            return result_array.tolist()
        except Exception:
            return mat
        
if __name__ == "__main__":
    s = Solution()

    mat = [[1,2],[3,4]]
    r = 1
    c = 4
    print(s.matrixReshape(mat, r, c))

    mat = [[1,2],[3,4]]
    r = 2
    c = 4
    print(s.matrixReshape(mat, r, c))