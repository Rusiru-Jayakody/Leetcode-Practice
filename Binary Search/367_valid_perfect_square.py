class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        l, r = 1, num // 2
        while l <= r:
            m = l + (r-l)//2
            guess = m * m
            if guess == num:
                return True
            elif guess < num:
                l = m + 1
            else:
                r = m - 1
        return False

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    num = int(input())
    ans = sol.isPerfectSquare(num)
    print(ans)