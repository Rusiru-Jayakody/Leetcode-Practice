class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        m, n = len(matrix), len(matrix[0]) 
        dp = {}
        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            best = 1
            for i_off, j_off in [(0,1), (0,-1), (1,0), (-1,0)]:
                r = i + i_off
                c = j + j_off
                if 0 <= r < m and 0 <= c < n and matrix[i][j] < matrix[r][c]:
                    best = max(best, 1 + dfs(r,c))
            dp[(i,j)] = best
            return best
        
        ans = 0
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i,j))

        return ans
            
            
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.
        
if __name__ == "__main__":
    sol = Solution()
    m, n = map(int, input().split())
    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    ans = sol.longestIncreasingPath(matrix)
    print(ans)            

        