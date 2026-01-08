from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        courses = prerequisites
        graph = defaultdict(list)
        for u,v in courses:
            graph[u].append(v)
        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        visits = [UNVISITED] * (numCourses)

        def dfs(i):
            if visits[i] == VISITED:
                return True
            if visits[i] == VISITING:
                return False
            visits[i] = VISITING
            for nei in graph[i]:
                if not dfs(nei):
                    return False
            visits[i] = VISITED
            return True
                    
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    n = int(input())
    prerequisites = []
    e = int(input())
    for _ in range(e):
        edge = list(map(int, input().split()))
        prerequisites.append(edge)
    ans = sol.canFinish(n, prerequisites)
    print(ans)
        

        
        