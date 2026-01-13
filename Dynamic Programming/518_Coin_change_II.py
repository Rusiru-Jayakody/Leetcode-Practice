class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]
        
        return dp[amount]
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    coins = list(map(int, input().split()))
    amount = int(input())
    ans = sol.change(amount, coins)
    print(ans)