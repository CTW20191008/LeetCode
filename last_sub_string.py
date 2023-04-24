######################################################################
# https://leetcode.cn/problems/last-substring-in-lexicographical-order/
######################################################################

class Solution:
    def lastSubstring(self, s: str) -> str:
        sub_str_list = []
        for i in range(0, len(s)):
            sub_str = ""
            for j in range(i, len(s)):
                sub_str = f"{sub_str}{s[j]}"
                if sub_str not in sub_str_list:
                    sub_str_list.append(sub_str)

        sorted_list = sorted(sub_str_list)

        return sorted_list[-1]
    

if __name__ == "__main__":
    solution = Solution()

    s = "abab"
    print(solution.lastSubstring(s))

    s = "leetcode"
    print(solution.lastSubstring(s))
