from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = Counter(magazine)
        for c in ransomNote:
            if c in dict and dict[c] > 0:
                dict[c] -= 1
            else:
                return False
        return True
     
        
#In the leecode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    r = input()
    m = input()
    ans = sol.canConstruct(r,m)
    print(ans)