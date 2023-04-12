######################################################################
# https://leetcode.cn/problems/median-of-two-sorted-arrays/
######################################################################

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        concat_list = nums1+nums2
        sorted_list = sorted(concat_list)

        if len(sorted_list)%2 == 0:
            i = int(len(sorted_list)/2)
            j = i-1
            return (sorted_list[i]+sorted_list[j])/2
        else:
            i = int(len(sorted_list)/2)
            return sorted_list[i]
        
if __name__ == "__main__":
    s = Solution()

    nums1 = [1,3]
    nums2 = [2]
    print(s.findMedianSortedArrays(nums1, nums2))

    nums1 = [1,2]
    nums2 = [3,4]
    print(s.findMedianSortedArrays(nums1, nums2))