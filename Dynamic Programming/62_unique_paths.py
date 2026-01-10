class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m):
            row = [0] * n
            dp.append(row)

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        return dp[m-1][n-1]
        
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    m, n = map(int, input().split())
    ans = sol.uniquePaths(m,n)
    print(ans)