######################################################################
# https://leetcode.cn/problems/pascals-triangle/
######################################################################

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result_list = [[1]]
        
        for i in range(1, numRows):
            sub_list = []
            for j in range(0, i+1):
                if j == 0:
                    sub_list.append(result_list[i-1][j])
                elif j == i:
                    sub_list.append(result_list[i-1][j-1])
                else:
                    sub_list.append(result_list[i-1][j-1]+result_list[i-1][j])

            result_list.append(sub_list)


        return result_list
    
if __name__ == "__main__":
    s = Solution()

    numRows = 5
    print(s.generate(numRows))

    numRows = 1
    print(s.generate(numRows))