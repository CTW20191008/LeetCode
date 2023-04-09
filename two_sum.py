######################################################################
## https://leetcode.cn/problems/two-sum/
######################################################################

from typing import List


class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     result_list = []
    #     for i in range(len(nums)):
    #         for j in range(i+1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 result_list.append(i)
    #                 result_list.append(j)
    #                 return result_list

    #     return result_list
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_list = []
        for first_index, first_value in enumerate(nums):
            second_value = target - first_value
            try:
                second_index = nums[first_index+1:].index(second_value)
                result_list.append(first_index)
                result_list.append(first_index+1+second_index)
                return result_list
            except Exception as e:
                pass

        return result_list


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))

    nums = [3, 2, 4]
    target = 6
    print(solution.twoSum(nums, target))

    nums = [3, 3]
    target = 6
    print(solution.twoSum(nums, target))
