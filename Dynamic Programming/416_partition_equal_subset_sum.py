class Solution:
    def canPartition(self, nums) -> bool:
        n = len(nums)
        if len(nums) == 1 or sum(nums)%2 == 1:
            return False
        
        target_sum = sum(nums)//2
        dp = set()
        dp.add(0)

        for num in nums:
            newDp = set()
            for t in dp:
                if t + num == target_sum:
                    return True
                newDp.add(t+num)
                newDp.add(t)
            dp = newDp
        
        return target_sum in dp
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int,input().split()))
    ans = sol.canPartition(nums)
    print(ans)



