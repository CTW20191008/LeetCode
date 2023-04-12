######################################################################
# https://leetcode.cn/problems/ransom-note/
######################################################################

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for ch in ransomNote:
            try:
                magazine.index(ch)
                magazine = magazine.replace(ch, "", 1)
            except Exception:
                return False
            
        return True
    
if __name__ == "__main__":
    s = Solution()

    ransomNote = "a"
    magazine = "b"
    print(s.canConstruct(ransomNote, magazine))

    ransomNote = "aa"
    magazine = "ab"
    print(s.canConstruct(ransomNote, magazine))

    ransomNote = "aa"
    magazine = "aab"
    print(s.canConstruct(ransomNote, magazine))

    ransomNote = "aab"
    magazine = "baa"
    print(s.canConstruct(ransomNote, magazine))