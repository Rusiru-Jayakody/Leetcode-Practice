class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        sett = set(jewels)
        for c in stones:
            if c in sett:
                count += 1
        return count
        
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    jewels = input()
    stones = input()
    ans = sol.numJewelsInStones(jewels, stones)
    print(ans)