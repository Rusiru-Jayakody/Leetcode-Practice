class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * (n)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        
        return dp[n-1]
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int, input().split()))
    ans = sol.rob(nums)
    print(ans)
        