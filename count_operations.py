######################################################################
# https://leetcode.cn/problems/count-operations-to-obtain-zero/
######################################################################

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        k = 0
        while num1 and num2:
            k += 1
            if num1 > num2:
                num1 = num1-num2
            else:
                num2 = num2-num1

        return k

if __name__ == "__main__":
    s = Solution()

    num1 = 2
    num2 = 3
    print(s.countOperations(num1, num2))

    num1 = 10
    num2 = 10
    print(s.countOperations(num1, num2))