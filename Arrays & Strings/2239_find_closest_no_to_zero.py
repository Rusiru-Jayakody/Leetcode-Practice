class Solution:
    def findClosestNumber(self, nums):

        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        
#In leetcode code editor you dint need to wite the following code.It is just to run in your local machine

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int, input().split()))

    ans = sol.findClosestNumber(nums)
    print(ans)
        