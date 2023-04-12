######################################################################
# https://leetcode.cn/problems/first-unique-character-in-a-string/
######################################################################

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0, len(s)):
            if s.count(s[i]) == 1:
                return i

        return -1

if __name__ == "__main__":
    solution = Solution()

    s = "leetcode"
    print(solution.firstUniqChar(s))

    s = "loveleetcode"
    print(solution.firstUniqChar(s))

    s = "aabb"
    print(solution.firstUniqChar(s))