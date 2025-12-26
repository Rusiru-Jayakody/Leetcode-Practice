class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        while l <= r:
            s[l], s[r] = s[r] , s[l]
            l += 1
            r -= 1

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    s = input().split()
    sol.reverseString(s)
    print(s)

        