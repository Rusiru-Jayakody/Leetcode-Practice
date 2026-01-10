class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+ 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    ans = sol.climbStairs(n)
    print(ans)