class Solution:
    def combine(self, n: int, k: int):
        ans , sol = [], [] 

        def backtrack(start):
            if len(sol) == k:
                ans.append(sol[:])
                return
            
            for i in range(start,n+1):
                sol.append(i)
                backtrack(i + 1)
                sol.pop()

        backtrack(1)
        return ans
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    n = int(input())
    k = int(input())
    ans = sol.combine(n,k)
    print(ans)