class Solution:
    def maxArea(self, height) -> int:
        maxx = 0
        l, r = 0, len(height)-1
        while l <= r:
            curr = min(height[l], height[r]) * (r-l)
            maxx = max(maxx, curr)
            if height[l] == height[r]:
                r -= 1
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxx

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    ans = sol.maxArea(nums)
    print(ans)
