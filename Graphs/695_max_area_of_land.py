class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        maxx = 0
        m = len(grid)
        n = len(grid[0])
        curr = 0

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i,j+1) + dfs(i, j-1) + dfs(i+1, j) + dfs(i-1,j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    curr = dfs(i,j)
                    maxx = max(maxx, curr)
        return maxx
    
#This is an alternative solution using iterative dfs
# class Solution:
#     def maxAreaOfIsland(self, grid) -> int:
#         maxx = 0
#         m = len(grid)
#         n = len(grid[0])
#         stk = []

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     stk.append((i,j))
#                     grid[i][j] = 0
#                     curr = 0
#                     while stk:
#                         r,c = stk.pop()
#                         curr += 1
#                         for i_off , j_off in [(1,0), (-1,0), (0,1), (0,-1)]:
#                             nr = r + i_off
#                             nc = c + j_off
#                             if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
#                                 stk.append((nr, nc))
#                                 grid[nr][nc] = 0
#                     maxx = max(maxx, curr)
#         return maxx

if __name__ == "__main__":

    sol = Solution()
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    ans = sol.maxAreaOfIsland(grid)
    print(ans)
        
        