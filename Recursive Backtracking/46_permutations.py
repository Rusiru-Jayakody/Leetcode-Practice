class Solution:
    def permute(self, nums):
        sol, res = [], []
        n  = len(nums)
        used = [False] * n

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            
            for j in range(n):
                if used[j]:
                    continue
                used[j] = True
                sol.append(nums[j ])
                backtrack()
                sol.pop()
                used[j] = False
        
        backtrack()
        return res
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int, input().split()))
    ans = sol.permute(nums)
    print(ans)
        