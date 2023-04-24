######################################################################
# https://leetcode.cn/problems/reverse-integer/
######################################################################

import math

class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x_str = str(-1*x)
            x_str_re = x_str[::-1]
            x_re = int(x_str_re)*(-1)
            if x_re < int(math.pow(-2, 31)):
                return 0
            else:
                return x_re
        else:
            x_str = str(x)
            x_str_re = x_str[::-1]
            x_re = int(x_str_re)
            if x_re > int(math.pow(2, 31)-1):
                return 0
            else:
                return x_re

        
if __name__ == "__main__":
    s = Solution()

    x = 123
    print(s.reverse(x))

    x = -123
    print(s.reverse(x))

    x = 120
    print(s.reverse(x))

    x = 0
    print(s.reverse(x))

    x = 1534236469
    print(s.reverse(x))