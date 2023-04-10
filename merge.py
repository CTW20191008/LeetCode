######################################################################
# https://leetcode.cn/problems/merge-sorted-array/
######################################################################

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        sub_nums1 = nums1[0:m]
        result_nums = sub_nums1 + nums2
        sort_result = sorted(result_nums)
        for i, value in enumerate(sort_result):
            nums1[i] = value

if __name__ == "__main__":
    s = Solution()

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1)
