class Solution:
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    l,r = l+1, r-1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif summ > 0:
                    r -= 1
                else:
                    l += 1
        return ans
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    ans = sol.threeSum(nums)
    print(ans)
            


        

        

        