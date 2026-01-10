class Solution:
    def coinChange(self, coins, amount: int) -> int:
        coins.sort()
        dp = [0] * (amount+1)

        for i in range(1,amount+1):
            minn = float('inf')
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                minn = min(minn, 1 + dp[diff])

            dp[i] = minn
        
        if dp[amount] < float('inf'):
            return dp[amount]
        else:
            return -1
        
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    coins = list(map(int, input().split()))
    amount = int(input())
    ans = sol.coinChange(coins, amount)
    print(ans)
        
        

        