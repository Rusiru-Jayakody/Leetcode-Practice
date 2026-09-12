class Solution:
    def mergeArrays(self, nums1, nums2) :
        x,y = 0, 0
        ans = []
        while x < len(nums1) and y < len(nums2):
            if nums1[x][0] == nums2[y][0]:
                ans.append([nums1[x][0],nums1[x][1] + nums2[y][1]])
                x += 1
                y += 1
            elif nums1[x][0] < nums2[y][0]:
                ans.append([nums1[x][0],nums1[x][1]])
                x += 1
            else:
                ans.append([nums2[y][0],nums2[y][1]])
                y += 1
        
        if x < len(nums1):
            for i in range(x,len(nums1)):
                ans.append(nums1[i])
        else:
            for i in range(y,len(nums2)):
                ans.append(nums2[i])
        
        return ans

            

        