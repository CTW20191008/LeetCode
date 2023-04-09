######################################################################
# https://leetcode.cn/problems/check-array-formation-through-concatenation/
######################################################################

from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        for piece in pieces:
            if all(item == 0 for item in arr):
                return True
            try:
                arr_index = arr.index(piece[0])
                sub_array = arr[arr_index:arr_index+len(piece)]
                if sub_array == piece:
                    for i in range(arr_index, arr_index+len(piece)):
                        arr[i] = 0
            except Exception as e:
                pass

        return all(item == 0 for item in arr)


if __name__ == "__main__":
    solution = Solution()

    arr = [15, 88]
    pieces = [[88], [15]]
    print(solution.canFormArray(arr, pieces))

    arr = [49, 18, 16]
    pieces = [[16, 18, 49]]
    print(solution.canFormArray(arr, pieces))

    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]
    print(solution.canFormArray(arr, pieces))
