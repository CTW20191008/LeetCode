######################################################################
# https://leetcode.cn/problems/roman-to-integer/
######################################################################

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        i = 0
        while i < len(s)-1:
            roman_int_c = roman_int_map[s[i]]
            roman_int_n = roman_int_map[s[i+1]]
            if roman_int_c < roman_int_n:
                result += roman_int_n-roman_int_c
                i += 2
            else:
                result += roman_int_c
                i += 1

        if i == len(s):
            return result
        else:
            return result + roman_int_map[s[len(s)-1]]


if __name__ == "__main__":
    solution = Solution()

    s = "III"
    print(solution.romanToInt(s))

    s = "IV"
    print(solution.romanToInt(s))

    s = "IX"
    print(solution.romanToInt(s))

    s = "LVIII"
    print(solution.romanToInt(s))

    s = "MCMXCIV"
    print(solution.romanToInt(s))
