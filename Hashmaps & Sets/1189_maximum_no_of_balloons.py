from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    s = input()
    ans = sol.maxNumberOfBalloons(s)
    print(ans)
        

                
            

        