class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        m = list()

        for i in range(min(len(word1), len(word2))):
            m.append(word1[i])
            m.append(word2[i])
        

        if len(word1) == len(word2):
            return "".join(m)

        elif len(word1) > len(word2):
            m.append(word1[len(word2):])
            return "".join(m)

        else:
            m.append(word2[len(word1):])
            return "".join(m)
        
#In the leecode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    word1 = input()
    word2 = input()

    ans = sol.mergeAlternately(word1,word2)
    print(ans)
        