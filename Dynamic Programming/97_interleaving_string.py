class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        dp = [[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True

        for i in range(m+1):
            for j in range(n+1):
                if i > 0 and dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
                if j > 0 and dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True

        return dp[m][n]
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    s1 = input()
    s2 = input()
    s3 = input()
    ans = sol.isInterleave(s1,s2,s3)
    print(ans)