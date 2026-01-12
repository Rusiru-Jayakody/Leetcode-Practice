class Solution:
    def maxProduct(self, nums) -> int:
        n = len(nums)
        dp = [[1,1] for _ in range(n)]
        dp[0][0] = dp[0][1] = nums[0]

        for i in range(1,n):
            if nums[i-1] == 0:
                dp[i][0] = nums[i]
                dp[i][1] = nums[i]
            else:     
                dp[i][0] = max(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i] )
                dp[i][1] = min(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i], nums[i] )
        
        maxx = float('-inf')
        for u,v in dp:
            maxx = max(maxx,u)
        
        return maxx
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int,input().split()))
    ans = sol.maxProduct(nums)
    print(ans)


        