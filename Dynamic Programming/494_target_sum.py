from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            newDp = defaultdict(int)
            for s in dp:
                newDp[s + num] += dp[s]
                newDp[s - num] += dp[s]
            dp = newDp

        return dp[target]

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int, input().split()))
    amount = int(input())
    ans = sol.findTargetSumWays(nums,amount)
    print(ans)        

        