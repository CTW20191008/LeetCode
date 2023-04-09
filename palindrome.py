######################################################################
# https://leetcode.cn/problems/palindrome-number/
######################################################################

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_str = str(x)
        while True:
            if len(x_str) <= 1:
                return True

            if x_str[0] == x_str[-1]:
                x_str = x_str[1 : len(x_str)-1]
            else:
                return False


if __name__ == "__main__":
    s = Solution()

    x = 121
    print(s.isPalindrome(x))

    x = -121
    print(s.isPalindrome(x))

    x = 10
    print(s.isPalindrome(x))