from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        seen = set()
        
        def dfs(node):
            if node == destination:
                return True
            seen.add(node)
            for nei in graph[node]:
                if nei not in seen:
                    if dfs(nei):
                        return True
            
            return False
        return dfs(source)
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    n = int(input())
    edges = []
    e = int(input())
    for _ in range(n):
        edge = list(map(int, input().split()))
        edges.append(edge)
    source, destination = map(int,input().split())
    ans = sol.validPath(n,edges,source, destination)
    print(ans)

        