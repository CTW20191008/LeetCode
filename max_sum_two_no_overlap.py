######################################################################
# https://leetcode.cn/problems/maximum-sum-of-two-non-overlapping-subarrays/
######################################################################

from typing import List

class Solution:
    def _max_sum(self, nums: list[int], length: int, drop_index=[-1, -1]) -> int:
        max_sum = 0

        for i in range(0, len(nums)+1-length):
            curr_max_sum = 0
            for j in range(i, i+length):
                if j >= drop_index[0] and j < drop_index[1]:
                    curr_max_sum = 0
                    break
                curr_max_sum += nums[j]

            if curr_max_sum > max_sum:
                max_sum = curr_max_sum

        return max_sum


    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        max_sum = 0
        for i in range(0, len(nums)+1-firstLen):
            curr_first_sum = 0
            for j in range(i, i+firstLen):
                curr_first_sum += nums[j]

            curr_second_sum_max = self._max_sum(nums, secondLen, [i, i+firstLen])
            if curr_first_sum + curr_second_sum_max > max_sum:
                max_sum = curr_first_sum + curr_second_sum_max

        return max_sum

    
if __name__ == "__main__":
    s = Solution()

    nums = [0,6,5,2,2,5,1,9,4]
    firstLen = 1
    secondLen = 2
    print(s.maxSumTwoNoOverlap(nums, firstLen, secondLen))

    nums = [3,8,1,3,2,1,8,9,0]
    firstLen = 3
    secondLen = 2
    print(s.maxSumTwoNoOverlap(nums, firstLen, secondLen))

    nums = [2,1,5,6,0,9,5,0,3,8]
    firstLen = 4
    secondLen = 3
    print(s.maxSumTwoNoOverlap(nums, firstLen, secondLen))

    nums = [4,5,14,16,16,20,7,13,8,15]
    firstLen = 3
    secondLen = 5
    print(s.maxSumTwoNoOverlap(nums, firstLen, secondLen))

    nums = [8,20,6,2,20,17,6,3,20,8,12]
    firstLen = 5
    secondLen = 4
    print(s.maxSumTwoNoOverlap(nums, firstLen, secondLen))
