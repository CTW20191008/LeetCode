######################################################################
# https://leetcode.cn/problems/number-of-times-binary-string-is-prefix-aligned/
######################################################################


class Solution(object):
    def numTimesAllBlue(self, flips):
        """
        :type flips: List[int]
        :rtype: int
        """
        number = 0
        left_num = 0
        curr_max_need = 0

        for index, flip in enumerate(flips):
            if curr_max_need <= flip:
                curr_max_need = flip

            flip = flip - 1
            print(f"index is {index}, flip is {flip}")
            if index < curr_max_need:
                left_num += 1

            if left_num == curr_max_need:
                print(f"left_num is {left_num}, curr_max_need is {curr_max_need}")
                number += 1

        return number

if __name__ == "__main__":
    solution = Solution()

    flips = [3,2,4,1,5]
    print(solution.numTimesAllBlue(flips))
