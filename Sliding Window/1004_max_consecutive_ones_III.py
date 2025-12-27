class Solution:
    def longestOnes(self, nums, k: int) -> int:
        max_window = 0
        zeros = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            curr_window = r-l+1
            max_window = max(max_window, curr_window)
        return max_window

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    k = int(input())
    ans = sol.longestOnes(nums,k)
    print(ans)
        