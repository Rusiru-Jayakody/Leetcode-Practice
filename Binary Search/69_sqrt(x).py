class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x
        while l <= r:
            m = l + (r-l)//2
            if (m*m) == x:
                return m
            elif (m*m) > x:
                r = m - 1
            else:
                l = m + 1
        return r

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    x = int(input())
    ans = sol.mySqrt(x)
    print(ans)