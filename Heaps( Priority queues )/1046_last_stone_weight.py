import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones,-(a-b))
        return -stones[-1] if stones else 0
    


#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":
    sol = Solution()
    stones = list(map(int,input().split()))
    ans = sol.lastStoneWeight(stones)
    print(ans)
        