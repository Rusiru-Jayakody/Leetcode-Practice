class Solution:
    def lengthOfLIS(self, nums) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

       

#Alternative soluiton with O(nlogn) time complexity
# from bisect import bisect_left

# class Solution:
#     def lengthOfLIS(self, nums):
#         tails = []

#         for num in nums:
#             idx = bisect_left(tails, num)

#             if idx == len(tails):
#                 tails.append(num)
#             else:
#                 tails[idx] = num

#         return len(tails)


#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int, input().split()))
    ans = sol.lengthOfLIS(nums)
    print(ans)