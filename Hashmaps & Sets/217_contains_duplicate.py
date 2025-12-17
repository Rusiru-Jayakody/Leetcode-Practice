class Solution:
    def containsDuplicate(self, nums) -> bool:
        sett = set()
        for c in nums:
            if c not in sett:
                sett.add(c)       
            else:
                return True
        return False


#In the leecode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    nums = list(map(int, input().split()))
    ans = sol.containsDuplicate(nums)
    print(ans)