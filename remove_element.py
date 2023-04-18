######################################################################
# https://leetcode.cn/problems/remove-element/
######################################################################

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, len(nums)-1
        while i <= j:
            if nums[i] == val:
                if nums[j] != val:
                    tmp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = tmp
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1

        return i
    
if __name__ == "__main__":
    s = Solution()

    nums = [3,2,2,3]
    val = 3
    print(s.removeElement(nums, val))

    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(s.removeElement(nums, val))