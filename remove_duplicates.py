######################################################################
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
######################################################################

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow = slow + 1
                nums[slow] = nums[fast]
            fast = fast + 1
        return slow + 1
    
if __name__ == "__main__":
    s = Solution()

    nums = [1,1,2]
    print(s.removeDuplicates(nums))

    nums = [0,0,1,1,1,2,2,3,3,4]
    print(s.removeDuplicates(nums))