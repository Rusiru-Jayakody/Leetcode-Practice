class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        d = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        n = len(digits)
        ans , sol = [], []

        def backtrack(i):
            if i == n:
                ans.append("".join(sol))
                return

            for c in d[digits[i]]:
                sol.append(c)
                backtrack(i+1)
                sol.pop()

        backtrack(0)
        return ans
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    digits = input()
    ans = sol.letterCombinations(digits)
    print(ans)
        