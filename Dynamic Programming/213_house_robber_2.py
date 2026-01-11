#Soluiton with tabulation approach
class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        def maxrob(arr):
            dp = [0] * len(arr)
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2,len(arr)):
                dp[i] = max(dp[i-1], dp[i-2]+arr[i])
            return dp[-1]

        return max(nums[0], maxrob(nums[1:]), maxrob(nums[:-1]))


        
#constant space solution
# class Solution:
#     def rob(self, nums) -> int:
#         n = len(nums)
        
#         def maxrob(arr):
#             r1, r2 = 0, 0
#             for num in arr:
#                 curr = max(r1 + num , r2)
#                 r1, r2 = r2, curr
#             return r2

#         return max(nums[0], maxrob(nums[1:]), maxrob(nums[:-1]))



#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int, input().split()))
    ans = sol.rob(nums)
    print(ans)


        