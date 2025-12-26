class Solution:
    def evalRPN(self, tokens) -> int:
        stk = []
        for c in tokens:
            if c in "+-/*":
                a = stk.pop()
                b = stk.pop()
                if c == "+":
                    stk.append(a + b)
                elif c == '-':
                    stk.append(b - a)
                elif c == '*':
                    stk.append(a * b)
                elif c == '/':
                    stk.append(int(b/a))
            else:
                stk.append(int(c))
        return stk.pop()

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    tokens = input().split()
    temp = sol.evalRPN(tokens)
    print(temp)
        