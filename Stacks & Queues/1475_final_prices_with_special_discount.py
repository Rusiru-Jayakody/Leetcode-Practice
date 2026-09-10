class Solution:
    def finalPrices(self, prices):
        ans = prices.copy()
        stk = []

        for i in range(len(prices)):
            while stk and prices[i] <= prices[stk[-1]]:
                ans[stk.pop()] -= prices[i]
            stk.append(i)
        
        return ans

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    prices = list(map(int,input().split()))
    ans = sol.finalPrices(prices)
    print(ans)