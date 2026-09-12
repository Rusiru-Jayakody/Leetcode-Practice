class Solution:
    def singleNonDuplicate(self, nums) -> int:
        l,r = 0, len(nums)-1
        if len(nums) == 1:
            return nums[0]
        while l <= r:
            if l == r and (l == 0 or l == len(nums)-1):
                return nums[l]
            m = l + (r-l)//2
            x = (m//2) + 1 
            
            if (m % 2 == 0 and nums[m+1] != nums[m]) or (m % 2 == 1 and nums[m-1] != nums[m]):
                r = m - 1
            else:
                l = m + 1
        return nums[l]

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int, input().split()))
    ans = sol.singleNonDuplicate(nums)
    print(ans)           
        