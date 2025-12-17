from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        d1 = Counter(s)
        d2 = Counter(t)

        for key, value in d1.items():
            if key in d2 and d2[key] == value:
                continue
            else:
                return False

        return True
        
       

#In the leecode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    s = input()
    t = input()
    ans = sol.isAnagram(s,t)
    print(ans)