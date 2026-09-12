class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x,y = 0,0
        while x < len(nums) and y < len(nums):
            if x < y:
                nums[x], nums[y] = nums[y],nums[x]
            else:
                y = x
            while y < len(nums) and nums[y] == 0:
                y += 1
            while x < len(nums) and nums[x] != 0:
                x += 1
        