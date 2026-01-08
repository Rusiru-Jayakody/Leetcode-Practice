from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        courses = prerequisites
        g = defaultdict(list)
        for u,v in courses:
            g[u].append(v)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses
        order = []

        def dfs(node):
            if states[node] == VISITED:
                return True
            
            if states[node] == VISITING:
                return False
            
            states[node] = VISITING
            for nei in g[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    n = int(input())
    prerequisites = []
    e = int(input())
    for _ in range(e):
        edge = list(map(int, input().split()))
        prerequisites.append(edge)
    ans = sol.findOrder(n, prerequisites)
    print(ans)
        


        