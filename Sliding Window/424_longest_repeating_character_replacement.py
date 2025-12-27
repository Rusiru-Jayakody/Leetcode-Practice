class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        l = 0
        longest = 0
        max_freq = 0
        for r in range(len(s)):
            idx = ord(s[r])-ord('A')
            counts[idx] += 1
            max_freq = max(max_freq, counts[idx])
            while (r-l+1) - max_freq > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1
            longest = max(longest, (r-l+1))
        return longest

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    s = input()
    k = int(input())
    ans = sol.characterReplacement(s,k)
    print(ans)