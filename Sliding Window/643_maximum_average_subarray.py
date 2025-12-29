class Solution:
    def findMaxAverage(self, nums, k: int) -> float:
        summ = 0
        for i in range(k):
            summ += nums[i]
        maxx = summ
        for i in range(k, len(nums)):
            summ += nums[i]
            summ -= nums[i-k]

            maxx = max(summ, maxx)
        return maxx/k
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    k = int(input())
    ans = sol.findMaxAverage(nums,k)
    print(ans)
        