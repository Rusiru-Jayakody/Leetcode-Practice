class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l,temp = 0,0
        for i in range(k):
            if blocks[i] == 'W':
                temp += 1
        minn = temp
        for r in range(k,len(blocks)):
            if blocks[r] == 'W':
                temp += 1
            if blocks[l] == 'W':
                temp -= 1
            l += 1
            minn = min(minn, temp)
        minn = min(temp,minn)
        return minn

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    blocks = input()
    k = int(input())
    ans = sol.minimumRecolors(blocks,k)
    print(ans)