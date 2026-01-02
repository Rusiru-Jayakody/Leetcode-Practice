import heapq
class Solution:
    def kClosest(self, points, k: int):
        heap = []
        for x,y in points:
            dist = x*x + y*y
            if len(heap) < k:
                heapq.heappush(heap,(-dist,x,y))
            else:
                if dist < -heap[0][0]:
                    heapq.heapreplace(heap,(-dist,x,y))
        return [[point[1],point[2]] for point in heap]
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":
    sol = Solution()
    points = []
    n = int(input()) #no of points
    for _ in range(n):
        points.append(list(map(int,input().split())))
    k = int(input())
    ans = sol.kClosest(points,k)
    print(ans)
        

        