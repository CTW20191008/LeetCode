######################################################################
# https://leetcode.cn/problems/longest-chunked-palindrome-decomposition/
######################################################################

class Solution:
    def longestDecomposition(self, text: str) -> int:
        k = 0
        i, j = 0, len(text)-1
        left_sub = ""
        right_sub = ""
        while i < j:
            left_ch = text[i]
            right_ch = text[j]
            if left_sub == "":
                left_sub = left_ch
                right_sub = right_ch

                if left_sub == right_sub:
                    k += 2
                    left_sub, right_sub = "", ""
            else:
                left_sub = f"{left_sub}{left_ch}"
                right_sub = f"{right_ch}{right_sub}"
                if left_sub == right_sub:
                    k += 2
                    left_sub, right_sub = "", ""

            i += 1
            j -= 1

        if left_sub != right_sub or i == j:
            return k+1
        else:
            return k
        
if __name__ == "__main__":
    s = Solution()

    text = "a"
    print(s.longestDecomposition(text))

    text = "aa"
    print(s.longestDecomposition(text))

    text = "aba"
    print(s.longestDecomposition(text))

    text = "ghiabcdefhelloadamhelloabcdefghi"
    print(s.longestDecomposition(text))

    text = "merchant"
    print(s.longestDecomposition(text))

    text = "antaprezatepzapreanta"
    print(s.longestDecomposition(text))
