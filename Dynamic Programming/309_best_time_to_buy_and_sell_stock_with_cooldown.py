class Solution:
    def maxProfit(self, prices
                  ) -> int:
        n = len(prices)
        hold = [0] * n
        sell = [0] * n
        cooldown = [0] * n

        hold[0] = -prices[0]
        sell[0] = float('-inf')

        for i in range(1,n):
            hold[i] = max(hold[i-1], cooldown[i-1] - prices[i])
            sell[i] = prices[i] + hold[i-1] 
            cooldown[i] = max(cooldown[i-1], sell[i-1])

        return max(sell[-1], cooldown[-1])     

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int, input().split()))
    ans = sol.maxProfit(nums)
    print(ans) 