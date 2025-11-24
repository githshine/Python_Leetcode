# 121. Best Time to Buy and Sell Stock

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # right = 0
        minPrince = float('inf') # 表示浮点数的无穷大 ∞
        profit = 0
        for price in prices:
            if price <= minPrince:
                minPrince = price
            else:
                # price > minPrince:
                profit = max(price - minPrince, profit)
        return profit
                
if __name__ == '__main__':
    obj = Solution()
    print(obj.maxProfit([7,1,5,3,6,4])) #5
    print(obj.maxProfit([7,6,4,3,1])) #0
    print(obj.maxProfit([7,2,4,3,4])) #0