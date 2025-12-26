class Solution:
    def dailyTemperatures(self, temperatures):
        stk = [0]
        ans = [0] * len(temperatures)
        for i in range(1,len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                ans[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        return ans

#In the leecode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    temperatures = list(map(int,input().split()))
    temp = sol.dailyTemperatures(temperatures)
    print(temp)



        