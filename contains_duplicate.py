######################################################################
# https://leetcode.cn/problems/contains-duplicate/
######################################################################

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(0, len(sorted_nums)-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True

        return False
    

if __name__ == "__main__":
    s = Solution()

    nums = [1,2,3,1]
    print(s.containsDuplicate(nums))

    nums = [1,2,3,4]
    print(s.containsDuplicate(nums))

    nums = [1,1,1,3,3,4,3,2,4,2]
    print(s.containsDuplicate(nums))