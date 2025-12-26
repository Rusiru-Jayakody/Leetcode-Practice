class Solution:
    def sortedSquares(self, nums):
        ans = []
        left, right = 0 , len(nums)-1
        while left <= right:
            if abs(nums[left]) >= abs(nums[right]):
                ans.append(nums[left] ** 2)
                left += 1
            else:
                ans.append(nums[right] ** 2)
                right -= 1
        ans.reverse()
        return ans

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    temp = sol.sortedSquares(nums)
    print(temp)
        