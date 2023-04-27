######################################################################
# https://leetcode.cn/problems/sort-the-people/
######################################################################

from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people_map = {}
        sorted_names = []
        for name, height in zip(names, heights):
            people_map[height] = name

        people_map_sorted = sorted(people_map.items(), key = lambda x:x[0], reverse=True)

        for people in people_map_sorted:
            sorted_names.append(people[1])

        return sorted_names
    
if __name__ == "__main__":
    s = Solution()

    names = ["Mary","John","Emma"]
    heights = [180,165,170]
    print(s.sortPeople(names, heights))

    names = ["Alice","Bob","Bob"]
    heights = [155,185,150]
    print(s.sortPeople(names, heights))
