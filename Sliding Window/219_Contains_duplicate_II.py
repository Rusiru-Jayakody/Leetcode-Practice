class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        s = set()
        l= 0
        
        for r in range(len(nums)):
            if r-l > k:
                s.remove(nums[l])
                l += 1
            if nums[r] in s:
                return True
            s.add(nums[r])
        
        return False

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int,input().split()))
    k = int(input())
    ans = sol.containsNearbyDuplicate(nums,k)
    print(ans)        
        