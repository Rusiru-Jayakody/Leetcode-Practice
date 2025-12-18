from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        d = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            d[key].append(s)
        return list(d.values())
    
#In the leecode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    strs = input().split()
    temp = sol.groupAnagrams(strs)
    print(temp)

    




                
                
        