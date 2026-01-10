class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        target = n-1

        for i in range(n-1,-1,-1):
            if nums[i] + i >= target:
                target = i

        return target == 0
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int, input().split()))
    ans = sol.canJump(nums)
    print(ans)


        