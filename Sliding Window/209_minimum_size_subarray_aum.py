#This soluiton works only when all the elements in the array are postive integers.If not we have to use prefix sums approach.

class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        shortest = float('inf')
        l = 0
        summ = 0
        for r in range(len(nums)):
            summ += nums[r]
            while summ >= target:
                shortest = min(shortest, (r-l+1))
                summ -= nums[l]
                l += 1
        return shortest if shortest < float('inf') else 0
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    k = int(input())
    ans = sol.minSubArrayLen(k,nums)
    print(ans)
        