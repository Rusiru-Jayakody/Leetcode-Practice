class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2,n+1):
            dp[i] = min(cost[i-1] + dp[i-1], cost[i-2] + dp[i-2])
        
        return dp[n]
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    cost = list(map(int, input().split()))
    ans = sol.minCostClimbingStairs(cost)
    print(ans)
        