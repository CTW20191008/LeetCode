######################################################################
# https://leetcode.cn/problems/check-if-two-string-arrays-are-equivalent/
######################################################################

from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1, w2 = "", ""
        for word in word1:
            w1 += word

        for word in word2:
            w2 += word

        if w1 == w2:
            return True
        else:
            return False
        
if __name__ == "__main__":
    s = Solution()

    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    print(s.arrayStringsAreEqual(word1, word2))

    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    print(s.arrayStringsAreEqual(word1, word2))

    word1  = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    print(s.arrayStringsAreEqual(word1, word2))