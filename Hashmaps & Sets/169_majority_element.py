from collections import Counter
class Solution:
    def majorityElement(self, nums) -> int:
        c = Counter(nums)
        maxx = 0
        ans = 0
        for key, value in c.items():
            if value > maxx:
                maxx = value
                ans = key
        return ans
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    ans = sol.majorityElement(nums)
    print(ans)


#The following is a solution with O(n) time complexity and O(1) space complexity.

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         ans = 0
#         count = 0
#         for c in nums:
#             if count == 0:
#                 ans = c
#             if ans == c:
#                 count += 1
#             else:
#                 count -= 1
#         return ans
                


        

        