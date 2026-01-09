class Solution:
    def pacificAtlantic(self, heights):
        m,n = len(heights), len(heights[0])
        atlantic = set()
        pacific = set()

        def dfs(i,j,visited):
            visited.add((i,j))
            for i_off, j_off in [(1,0), (-1,0), (0,1), (0,-1)]:
                r = i + i_off
                c = j + j_off
                if (r,c) not in visited and 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j]:
                    dfs(r,c,visited)
        
        #atlantic
        for i in range(m):
            dfs(i,n-1,atlantic)           
        for j in range(n-1):
            dfs(m-1,j,atlantic)

        #pacific
        for i in range(m):
            dfs(i,0,pacific)           
        for j in range(1,n):
            dfs(0,j,pacific)

        return list(pacific & atlantic)
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    n = int(input())
    heights = []
    for _ in range(n):
        row = list(map(int, input().split()))
        heights.append(row)
    ans = sol.pacificAtlantic(heights)
    print(ans)
            

        

        
        
        

        