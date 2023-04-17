######################################################################
# https://leetcode.cn/problems/longest-common-prefix/
######################################################################

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result_prefix = ""
        curr_char = ""
        curr_prefix_index = 0
        while True:
            for s_str in strs:
                if curr_prefix_index < len(s_str):
                    if curr_char == "":
                        curr_char = s_str[curr_prefix_index]
                    else:
                        if curr_char != s_str[curr_prefix_index]:
                            return result_prefix
                else:
                    return result_prefix
                
            result_prefix = f"{result_prefix}{curr_char}"
            curr_char = ""
            curr_prefix_index += 1

if __name__ == "__main__":
    s = Solution()

    strs = ["flower","flow","flight"]
    print(s.longestCommonPrefix(strs))

    strs = ["dog","racecar","car"]
    print(s.longestCommonPrefix(strs))
