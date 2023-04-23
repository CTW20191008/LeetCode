######################################################################
# https://leetcode.cn/problems/longest-palindromic-substring/
######################################################################

class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        longest_sub_str = ""
        while len(s) - i > len(longest_sub_str):
            j = len(s) - 1
            left_index = i
            right_index = j
            begin_sub_str = False
            while left_index < right_index:
                if begin_sub_str:
                    if s[left_index] == s[right_index]:
                        left_index += 1
                        right_index -= 1
                    else:
                        begin_sub_str = False
                        j -= 1
                        right_index = j
                        left_index = i
                        continue
                else:
                    if s[left_index] == s[right_index]:
                        begin_sub_str = True
                        j = right_index
                        left_index += 1
                        right_index -= 1
                    else:
                        right_index -= 1

            if begin_sub_str:
                curr_sub_str = s[i: j+1]
                if len(curr_sub_str) > len(longest_sub_str):
                    longest_sub_str = curr_sub_str

            i += 1

        if len(longest_sub_str) < 1:
            longest_sub_str = s[0]
        return longest_sub_str

if __name__ == "__main__":
    solution = Solution()

    s = "babad"
    print(solution.longestPalindrome(s))

    s = "cbbd"
    print(solution.longestPalindrome(s))

    s = "ac"
    print(solution.longestPalindrome(s))

    s = "aacabdkacaa"
    print(solution.longestPalindrome(s))
