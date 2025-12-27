class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_w = 0
        l = 0
        sett = set()
        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1           
            sett.add(s[r])
            curr_w = r -l + 1
            max_w = max(max_w, curr_w)
        return max_w

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    s = input()
    ans = sol.lengthOfLongestSubstring(s)
    print(ans)