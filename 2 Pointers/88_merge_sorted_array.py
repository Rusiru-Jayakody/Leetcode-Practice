class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        x,y,last = m-1,n-1,(m+n)-1

        while y >= 0:
            if x >= 0 and nums1[x] > nums2[y]:
                nums1[last] = nums1[x]
                x -= 1
            else:
                nums1[last] = nums2[y]
                y -= 1
            last -= 1

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    m = int(input())
    n = int(input())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    ans = sol.merge(nums1,m,nums2,n)
    print(ans)