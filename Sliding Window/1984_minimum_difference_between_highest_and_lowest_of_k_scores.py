class Solution:
    def minimumDifference(self, nums, k: int) -> int:
        nums.sort()
        min_diff = nums[k-1] - nums[0]

        l = 0
        for r in range(k-1,len(nums)):
            min_diff = min(min_diff,nums[r] - nums[l])
            r += 1
            l += 1
        return min_diff

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int, input().split()))
    k = int(input())
    ans = sol.minimumDifference(nums,k)
    print(ans)