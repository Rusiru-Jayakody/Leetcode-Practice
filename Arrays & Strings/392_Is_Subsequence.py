class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        
        p = 0
        for i in range(len(t)):
            if p == len(s):
                return True
            if t[i] == s[p]:
                p += 1
        return p == len(s)


#In the leecode code editor you dont need to write the following code . It is just to run in your local machine.
if __name__ == "__main__":
    s = input()
    t = input()

    sol = Solution()                 # create object
    ans = sol.isSubsequence(s, t)    # call method
    print(ans)
