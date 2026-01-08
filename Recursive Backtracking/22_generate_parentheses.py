class Solution:
    def generateParenthesis(self, n: int):
        res, sol = [], []

        def backtrack(openn, close):
            if len(sol) == 2*n:
                res.append("".join(sol))
                return
            
            if openn < n:
                sol.append('(')
                backtrack(openn+1,close)
                sol.pop()

            if openn > close:
                sol.append(')')
                backtrack(openn, close+1)
                sol.pop()

        backtrack(0,0)
        return res
        
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    n = int(input())
    ans = sol.generateParenthesis(n)
    print(ans)