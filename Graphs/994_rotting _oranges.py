from collections import deque
class Solution:
    def orangesRotting(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        time = 0
        fresh_count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return time

        while q and fresh_count > 0:
            l = len(q)
            for _ in range(l):
                i,j = q.popleft()
                for i_off, j_off in [(1,0), (-1,0), (0,1), (0,-1)]:
                    r = i + i_off
                    c = j + j_off
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        q.append((r,c))
                        grid[r][c] = 2
                        fresh_count -= 1
            time += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return time


#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    ans = sol.orangesRotting(grid)
    print(ans)
            