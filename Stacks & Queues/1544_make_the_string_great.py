class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for c in s:
            stk.append(c)
            while len(stk) >= 2 and (stk[-1] != stk[-2]) and (stk[-1] == stk[-2].lower() or stk[-1] == stk[-2].upper()):
                stk.pop()
                stk.pop()
        return "".join(stk)
                
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    s = input()
    ans = sol.makeGood(s)
    print(ans)