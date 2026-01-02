This is an alternative solution with O(n) run time complexity
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
        