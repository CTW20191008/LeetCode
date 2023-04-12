######################################################################
# https://leetcode.cn/problems/valid-sudoku/
######################################################################

from typing import List


class Solution:
    def _check_list(self, sub_list):
        for i in range(1, 10):
            if sub_list.count(f"{i}") > 1:
                return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for sub_list in board:
            if not self._check_list(sub_list):
                return False

        for i in range(0, 9):
            sub_list = []
            for j in range(0, 9):
                sub_list.append(board[j][i])
            if not self._check_list(sub_list):
                return False

        for i in range(0, 3):
            for j in range(0, 3):
                sub_list = []
                for m in range(i*3, i*3+3):
                    for n in range(j*3, j*3+3):
                        sub_list.append(board[m][n])

                if not self._check_list(sub_list):
                    return False

        return True


if __name__ == "__main__":
    s = Solution()

    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"], 
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"], 
             [".", "6", ".", ".", ".", ".", "2", "8", "."], 
             [".", ".", ".", "4", "1", "9", ".", ".", "5"], 
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(s.isValidSudoku(board))
    
    board = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]
    print(s.isValidSudoku(board))
