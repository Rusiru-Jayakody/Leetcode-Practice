class Solution:
    def twoSum(self, nums , target: int):
        d = {}

        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            y = target - nums[i]
            if y in d and d[y] != i:
                return [i, d[y]]
            
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int, input().split()))
    target = int(input())
    ans = sol.twoSum(nums, target)
    print(ans)


       
        