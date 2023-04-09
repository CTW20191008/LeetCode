######################################################################
# https://leetcode.cn/problems/get-maximum-in-generated-array/
######################################################################


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n in [0, 1]:
            return n

        nums = [0]*(n+1)
        nums[0] = 0
        nums[1] = 1
        max_value = 1
        for i in range(2, n+1):
            if i%2 == 0:
                nums[i] = nums[int(i/2)]
            else:
                nums[i] = nums[int(i/2)] + nums[int((i+1)/2)]

            if nums[i] > max_value:
                max_value = nums[i]

        return max_value
    

if __name__ == "__main__":
    s = Solution()
    
    n = 7
    print(s.getMaximumGenerated(n))

    n = 2
    print(s.getMaximumGenerated(n))

    n = 3
    print(s.getMaximumGenerated(n))
