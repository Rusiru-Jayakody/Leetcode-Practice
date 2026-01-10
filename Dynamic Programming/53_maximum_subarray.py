class Solution:
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        maxx = nums[0]

        for i in range(1,n):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
            maxx = max(maxx,dp[i])       
        return maxx
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int, input().split()))
    ans = sol.maxSubArray(nums)
    print(ans)