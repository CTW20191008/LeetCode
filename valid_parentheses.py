######################################################################
# https://leetcode.cn/problems/valid-parentheses/
######################################################################

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                q.append(ch)
            else:
                if len(q) == 0:
                    return False

                ch_p = q.pop()
                pare = f"{ch_p}{ch}"
                if pare not in ["()", "[]", "{}"]:
                    return False
                
        if len(q) != 0:
            return False
                
        return True
    
if __name__ == "__main__":
    solution = Solution()

    s = "()"
    print(solution.isValid(s))

    s = "()[]{}"
    print(solution.isValid(s))

    s = "(]"
    print(solution.isValid(s))

    s = "["
    print(solution.isValid(s))