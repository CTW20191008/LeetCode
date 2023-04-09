######################################################################
# https://leetcode.cn/problems/check-distances-between-same-letters/
######################################################################

from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        ch_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                   'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
                   'w', 'x', 'y', 'z']
        right_dist = [0]*len(distance)
        for i, ch in enumerate(ch_list):
            first_index = s.find(ch)
            if -1 != first_index:
                second_index = s.rfind(ch)
                right_dist[i] = second_index - first_index - 1
            else:
                right_dist[i] = distance[i]

        for i in range(len(distance)):
            if distance[i] != right_dist[i]:
                return False

        return True


if __name__ == "__main__":
    solution = Solution()

    s = "abaccb"
    distance = [1, 3, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(solution.checkDistances(s, distance))

    s = "aa"
    distance = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(solution.checkDistances(s, distance))
