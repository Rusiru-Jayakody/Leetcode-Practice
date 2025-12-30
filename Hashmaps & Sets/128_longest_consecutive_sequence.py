class Solution:
    def longestConsecutive(self, nums) -> int:
        s = set(nums)
        maxx = 0
        for c in s:
            if c-1 not in s:
                curr = 1
                next = c + 1
                while next in s:
                    curr += 1
                    next += 1
                maxx = max(curr, maxx)
        return maxx

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    ans = sol.longestConsecutive(nums)
    print(ans)
        