class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        n = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > n:
                    res = s[l:r+1]
                    n = r-l+1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > n:
                    res = s[l:r+1]
                    n = r-l+1
                l -= 1
                r += 1
        
        return res
        
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    s = input()
    ans = sol.longestPalindrome(s)
    print(ans)