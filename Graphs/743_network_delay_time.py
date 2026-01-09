from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times, n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,t in times:
            graph[u].append((v,t))
        
        mintimes = {}
        heap = [(0,k)]

        while heap:
            k_to_i, i = heapq.heappop(heap)
            if i in mintimes:
                continue
            mintimes[i] = k_to_i

            for nei, nei_t in graph[i]:
                if nei not in mintimes:
                    heapq.heappush(heap,(k_to_i + nei_t, nei))
        if len(mintimes) == n:
            return max(mintimes.values())
        return -1



#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    edges = []
    e = int(input())
    for _ in range(e):
        edge = list(map(int, input().split()))
        edges.append(edge)
    k = int(input())
    ans = sol.networkDelayTime(edges,n,k)
    print(ans)

