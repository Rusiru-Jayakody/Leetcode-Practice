class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False

        window = [0] * 26
        need = [0] * 26

        for i in range(len(s1)):
            window[ord(s1[i]) - ord('a')] += 1
            need[ord(s2[i]) - ord('a')] += 1

        if window == need:
            return True

        for i in range(len(s1),len(s2)):
            need[ord(s2[i]) - ord('a')] += 1
            need[ord(s2[i - len(s1)]) - ord('a')] -= 1
            if window == need:
                return True
        return False

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    s1 = input()
    s2 = input()
    ans = sol.checkInclusion(s1,s2)
    print(ans)