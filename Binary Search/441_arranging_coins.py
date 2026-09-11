class Solution:
    def arrangeCoins(self, n: int) -> int:
        l,r = 1,n
        while l <= r:
            m = l + (r-l)//2
            needed = (m*(m+1))//2
            if needed == n:
                return m
            elif n < needed:
                r = m - 1
            else:
                l = m + 1
        return r

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    n = int(input())
    ans = sol.arrangeCoins(n)
    print(ans)