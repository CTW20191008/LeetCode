######################################################################
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
######################################################################

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = ""
        longest_sub_str_length = 0
        i, j = 0, 0
        while i < len(s) and j < len(s):
            if s[j] not in sub_str:
                sub_str = f"{sub_str}{s[j]}"
                j += 1
            else:
                sub_str_length = len(sub_str)
                if sub_str_length > longest_sub_str_length:
                    longest_sub_str_length = sub_str_length

                sub_str = ""
                i += 1
                j = i

                if i + longest_sub_str_length >= len(s):
                    break

        if len(sub_str) > longest_sub_str_length:
            return len(sub_str)
        else:
            return longest_sub_str_length


if __name__ == "__main__":
    solution = Solution()

    s = "abcabcbb"
    print(solution.lengthOfLongestSubstring(s))

    s = "bbbbb"
    print(solution.lengthOfLongestSubstring(s))

    s = "pwwkew"
    print(solution.lengthOfLongestSubstring(s))

    s = " "
    print(solution.lengthOfLongestSubstring(s))
