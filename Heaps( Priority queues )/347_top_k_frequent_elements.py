from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums, k: int):
        c = Counter(nums)
        heap = []
        for key,v in c.items():
            if len(heap) < k:
                heapq.heappush(heap,(v,key))
            else:
                heapq.heappushpop(heap,(v,key))
        return [s[1] for s in heap]
    
# This is an alternative solution with O(n) run time complexity
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums, k: int):
#         c = Counter(nums)
#         buckets = [0] * (len(nums) +1)
#         for key, val in c.items():
#             if buckets[val] == 0:
#                 buckets[val] = [key]
#             else:
#                 buckets[val].append(key)
#         ans = []
#         for i in range(len(nums),-1,-1):
#             if buckets[i] != 0:
#                 ans.extend(buckets[i])
#             if len(ans) == k:
#                 break
#         return ans
        
    

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":
    sol = Solution()
    nums = list(map(int,input().split()))
    k = int(input())
    ans = sol.topKFrequent(nums,k)
    print(ans)
        