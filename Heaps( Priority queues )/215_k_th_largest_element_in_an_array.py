import heapq
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        return nums[0]


# Better solution with O(nlogk).
# import heapq
# class Solution:
#     def findKthLargest(self, nums, k: int) -> int:
#         heap = nums[:k]
#         heapq.heapify(heap)
#         for i in range(k,len(nums)):
#             heapq.heappushpop(heap,nums[i])
#         return heap[0]

    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int,input().split()))
    k = int(input())
    ans = sol.findKthLargest(nums,k)
    print(ans)
        