class Solution:
    def summaryRanges(self, nums):
        ans = list()
        temp = list()
        if len(nums) == 0:
            return []
        start, end = nums[0], nums[0]
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == end:
                    ans.append(str(start))
                else:
                    ans.append("->".join(map(str,[start,end])))
                start, end = nums[i],nums[i]
            else:
                end = nums[i]

        if end == nums[-1] and start != end:
            ans.append("->".join(map(str, [start, end])))
        else:
            ans.append(str(end))
        
        return ans
        
            
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    ans = sol.summaryRanges(nums)
    print(ans)

