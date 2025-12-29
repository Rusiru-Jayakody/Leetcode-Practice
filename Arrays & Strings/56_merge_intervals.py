class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key = lambda x : x[0])
        ans = [intervals[0]]
        for curr in intervals[1:]:
            if curr[0] <= ans[-1][1]:   
                ans[-1][1] = max(ans[-1][1], curr[1])
            else:
                ans.append(curr)
        return ans
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    n = int(input())
    intervals = []
    for _ in range(n):
        intervals.append(list(map(int,input().split())))
    ans = sol.merge(intervals)
    print(ans)