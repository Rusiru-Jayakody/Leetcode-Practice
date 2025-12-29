from math import ceil
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l)//2
            t = 0
            for n in piles:
                t += ceil(n/m)
            if t > h:
                l = m + 1
            else:
                r = m
        return l
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    piles = list(map(int,input().split()))
    h = int(input())
    ans = sol.minEatingSpeed(piles,h)
    print(ans)