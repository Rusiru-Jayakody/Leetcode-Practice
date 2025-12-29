import random

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = l + (r-l) //2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l


#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    n = int(input())  
    BAD_VERSION = random.randint(1, n)  # Random bad version in 1..n

    # Define the API to match LeetCode
    def isBadVersion(version):
        return version >= BAD_VERSION

    sol = Solution()
    ans = sol.firstBadVersion(n)
    print(ans)