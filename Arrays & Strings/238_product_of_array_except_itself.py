class Solution:
    def productExceptSelf(self, nums):
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        ans = [1] * len(nums)
        for i in range(len(nums)):
            j = -i-1
            if i == 0:
                continue
            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[j] = nums[j+1] * suffix[j+1]
        for i in range(len(nums)):
            ans[i] = prefix[i] * suffix[i]
        return ans

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    ans = sol.productExceptSelf(nums)
    print(ans)



#Constant space solution

# class Solution:
#     def productExceptSelf(self, nums):
#         n = len(nums)
#         ans = [1] * n
        
#         # 1) Build prefix products directly in ans
#         for i in range(1, n):
#             ans[i] = ans[i-1] * nums[i-1]
        
#         # 2) Multiply by suffix products on the fly
#         suffix = 1
#         for i in range(n-1, -1, -1):
#             ans[i] *= suffix
#             suffix *= nums[i]
        
#         return ans

        