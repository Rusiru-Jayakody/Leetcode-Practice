class Solution:
    def calPoints(self, operations) -> int:
        stk = []
        for c in operations:
            if c == "+":
                if len(stk)>1:
                    stk.append(stk[-1] + stk[-2])
            elif c == "C":
                if stk:
                    stk.pop()
            elif c == "D":
                if stk:
                    stk.append(stk[-1]*2)
            else:
                stk.append(int(c))
        return sum(stk)
    
#In the leecode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    operations = input().split()
    temp = sol.calPoints(operations)
    print(temp)