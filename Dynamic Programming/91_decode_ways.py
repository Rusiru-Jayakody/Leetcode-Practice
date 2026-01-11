class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]  == '0':
            return 0
        dp = [0] * (len(s)+1)
        dp[0] = 1

        for i in range(len(s)):
            if s[i] == '0':
                dp[i+1] = 0
            
            else:
                dp[i+1] = dp[i]

            if (i-1 >= 0) and s[i-1] != '0' and int("".join([s[i-1],s[i]])) <= 26:
                dp[i+1] += dp[i-1]

        return dp[-1]

        
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    s = input()
    ans = sol.numDecodings(s)
    print(ans)