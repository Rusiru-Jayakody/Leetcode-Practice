class Solution:
    def longestCommonPrefix(self, strs) -> str:
        s = sorted(strs, key = len)
        n = len(s[0])

        if n == 0:
            return ""

        for i in range(n):
            for str in s:
                if s[0][i] != str[i]:
                    return s[0][:i]
        
        return s[0]
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    strs = input().split()
    ans = sol.longestCommonPrefix(strs)
    print(ans)

