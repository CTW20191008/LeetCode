######################################################################
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
######################################################################

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price, min_price = prices[0], prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                sub_max_profit = max_price - min_price
                if sub_max_profit > max_profit:
                    max_profit = sub_max_profit
                max_price = min_price = prices[i]
            else:
                if prices[i] > max_price:
                    max_price = prices[i]

        last_max_profit = max_price - min_price
        if last_max_profit > max_profit:
            max_profit = last_max_profit

        return max_profit
    
if __name__ == "__main__":
    s = Solution()

    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))

    prices = [7,6,4,3,1]
    print(s.maxProfit(prices))