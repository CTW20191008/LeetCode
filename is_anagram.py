######################################################################
# https://leetcode.cn/problems/valid-anagram/
######################################################################

class Solution:
    def isAnagram_old(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for ch in s:
            try:
                t.index(ch)
                t = t.replace(ch, "", 1)
            except Exception:
                return False
            
        return True
    
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True

        return False
    
if __name__ == "__main__":
    solution = Solution()

    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))

    s = "rat"
    t = "car"
    print(solution.isAnagram(s, t))