class Solution:
    def minOperations(self, logs) -> int:
        stk = []
        for s in logs:
            if s == "../":
                if stk:
                    stk.pop()
            elif s == "./":
                pass
            else:
                stk.append(s)
        return len(stk) 

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    logs = list(input().split())
    ans = sol.minOperations(logs)
    print(ans)