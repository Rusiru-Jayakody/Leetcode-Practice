class Solution:
    def twoSum(self, numbers, target: int):
        l, r = 0, len(numbers)-1
        while l < r:
            x = numbers[l] + numbers[r]
            if x == target:
                return [l+1,r+1]
            elif x < target:
                l += 1
            else:
                r -= 1

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    target = int(input())
    ans = sol.twoSum(nums, target)
    print(ans)



        