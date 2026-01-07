class Solution:
    def combinationSum(self, candidates, target: int) :
        ans , sol = [], []
        
        def backtrack(i,curr_sum):
            if curr_sum == target :
                ans.append(sol[:])
                return
            if curr_sum > target or i == len(candidates):
                return
            backtrack(i+1, curr_sum)
            sol.append(candidates[i])
            backtrack(i,curr_sum + candidates[i])
            sol.pop()

        backtrack(0,0)
        return ans
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    candidates = list(map(int, input().split()))
    target = int(input())
    ans = sol.combinationSum(candidates,target)
    print(ans)
        