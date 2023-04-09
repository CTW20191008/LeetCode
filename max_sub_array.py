######################################################################
# https://leetcode.cn/problems/maximum-subarray/
######################################################################

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_sum = nums[0]
        curr_sub_sum = nums[0]

        for i in range(1, len(nums)):
            if curr_sub_sum <= 0:
                if curr_sub_sum < nums[i]:
                    curr_sub_sum = nums[i]
            else:
                curr_sub_sum += nums[i]

            if curr_sub_sum > max_sub_sum:
                max_sub_sum = curr_sub_sum

            if curr_sub_sum <= 0:
                curr_sub_sum = -10001

        return max_sub_sum


if __name__ == "__main__":
    s = Solution()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(s.maxSubArray(nums))

    nums = [1]
    print(s.maxSubArray(nums))

    nums = [5, 4, -1, 7, 8]
    print(s.maxSubArray(nums))

    nums = [-2, 1]
    print(s.maxSubArray(nums))

    nums = [-2, -3, -1]
    print(s.maxSubArray(nums))
