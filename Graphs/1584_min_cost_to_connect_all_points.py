import heapq
class Solution:
    def minCostConnectPoints(self, points) -> int:
        n = len(points)
        seen = set()
        heap = [(0,0)]
        cost = 0

        while len(seen) < n:
            dist, i = heapq.heappop(heap)
            if i in seen:
                continue
            seen.add(i)
            cost += dist
            xi, yi = points[i]

            for j in range(n):
                if j not in seen:
                    xj, yj = points[j]
                    manh_dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(heap,(manh_dist, j))
        return cost




#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    points = []
    for _ in range(n):
        point = list(map(int, input().split()))
        points.append(point)
    ans = sol.minCostConnectPoints(points)
    print(ans)
