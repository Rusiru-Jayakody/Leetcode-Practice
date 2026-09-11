class Solution:
    def maxSatisfied(self, customers, grumpy, minutes: int) -> int:
        count,l = 0, 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                count += customers[i]

        maxx, curr = 0, 0
        for i in range(minutes):
            if grumpy[i] == 1:
                curr += customers[i]
        
        maxx = curr
        for r in range(minutes,len(grumpy)):
            if grumpy[r] == 1:
                curr += customers[r]
            if grumpy[l] == 1:
                curr -= customers[l]
            maxx = max(maxx,curr)
            l += 1
        return (maxx + count)

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    customers = list(map(int, input().split()))
    grumpy = list(map(int, input().split()))
    minutes = int(input())
    ans = sol.maxSatisfied(customers,grumpy,minutes)
    print(ans)