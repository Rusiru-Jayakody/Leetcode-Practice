class Solution:
    def isValid(self, s1: str) -> bool:
        d = {')':'(', '}':'{', ']':'['}
        stk = []
        for c in s1:
            if c in "([{":
                stk.append(c)
            elif not stk or stk.pop() != d[c]:
                return False
        return not stk
    
#In the leecode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    s1 = input()
    temp = sol.isValid(s1)
    print(temp)
