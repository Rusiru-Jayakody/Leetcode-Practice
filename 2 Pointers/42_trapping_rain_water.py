class Solution:
    def trap(self, height) -> int:
        summ = 0
        left = [0]*len(height)
        right = [0]*len(height)
        l = r = 0

        for i in range(len(height)):
            j = -i - 1
            left[i] = l
            right[j] = r
            l = max(l, height[i])
            r = max(r, height[j])

        for i in range(len(height)):
            minn = min(left[i], right[i])
            if minn > height[i]:
                summ += minn - height[i]
        return summ

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    height = list(map(int,input().split()))
    ans = sol.trap(height)
    print(ans)
        

        



        