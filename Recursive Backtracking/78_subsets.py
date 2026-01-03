class Solution:
    def subsets(self, nums):
        n = len(nums)
        res , sol = [], []
        def backtrack(i):
            if i == n:
                res.append(sol[:])   #appending a snapshot of the sol at the moment
                return
            #do not pick nums[i]
            backtrack(i+1)

            #pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        backtrack(0)
        return res
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int, input().split()))
    ans = sol.subsets(nums)
    print(ans)
        