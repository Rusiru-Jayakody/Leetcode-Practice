class Solution:
    def maxProfit(self, prices) :

        profit = 0
        minn = prices[0]

        for price in prices:
            if price > minn:
                profit = max(profit, price - minn)
            else:
                minn = price

        return profit
    
#In the leecode code editor you dont need to write the following code . It is just to run in your local machine.

prices = list(map(int, input().split()))
sol = Solution()
ans = sol.maxProfit(prices)
print(ans)

      
        