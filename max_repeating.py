######################################################################
# https://leetcode.cn/problems/maximum-repeating-substring/
######################################################################

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        new_word = word
        while True:
            if new_word in sequence:
                k += 1
                new_word = new_word+word
            else:
                break

        return k


if __name__ == "__main__":
    s = Solution()

    sequence = "ababc"
    word = "ab"
    print(s.maxRepeating(sequence, word))

    sequence = "ababc"
    word = "ba"
    print(s.maxRepeating(sequence, word))

    sequence = "ababc"
    word = "ac"
    print(s.maxRepeating(sequence, word))

    sequence = "aaabaaaabaaabaaaabaaaabaaaabaaaaba"
    word = "aaaba"
    print(s.maxRepeating(sequence, word))
