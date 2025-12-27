class Solution:
    def searchInsert(self, nums, target: int) -> int:
        l, r = 0, len(nums) -1
        while l <= r:
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return l
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    target = int(input())
    ans = sol.searchInsert(nums, target)
    print(ans)
        