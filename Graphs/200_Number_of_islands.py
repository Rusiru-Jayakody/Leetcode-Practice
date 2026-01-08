class Solution:
    def numIslands(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        count = [0]

        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for i_off, j_off in [(0,1),(0,-1), (1,0), (-1,0)]:
                r = i + i_off
                c = j + j_off
                dfs(r,c)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count[0] += 1
                    dfs(i, j)
        return count[0]
    
#This is a alternative solution using BFS
# from collections import deque
# class Solution:
#     def numIslands(self, grid) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         count = 0
#         q = deque()

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "1":
#                     count += 1
#                     q.append((i,j))
#                     grid[i][j] = "0"

#                     while q:
#                         r, c = q.popleft()
#                         for i_off, j_off in [(0,1),(0,-1), (1,0), (-1,0)]:
#                             r_new = r + i_off
#                             c_new = c + j_off
#                             if 0<= r_new < m and 0 <= c_new < n and grid[r_new][c_new] == "1":
#                                 grid[r_new][c_new] = "0"
#                                 q.append((r_new,c_new))
#         return count


#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    ans = sol.numIslands(grid)
    print(ans)
        