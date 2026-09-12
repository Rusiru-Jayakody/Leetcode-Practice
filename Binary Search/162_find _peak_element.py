class Solution:
    def findPeakElement(self, nums) -> int:
        l,r = 0, len(nums) - 1
        while l < r:
            m = l + (r-l)//2
            if (m-1) >= 0 and nums[m] <= nums[m-1]:
                r = m
            elif (m + 1) <= len(nums) - 1 and nums[m] <= nums[m+1]:
                l = m + 1
            else:
                return m
        return l
         
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int, input().split()))
    ans = sol.findPeakElement(nums)
    print(ans)