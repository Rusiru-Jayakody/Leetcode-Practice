class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:
        summ,l,count = 0, 0, 0
        for i in range(k):
            summ += arr[i]
        
        count += 1 if summ >= (k * threshold) else 0

        for r in range(k,len(arr)):
            summ += (arr[r] - arr[l])
            l += 1
            count += 1 if summ >= (threshold *k) else 0
        
        return count

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    arr = list(map(int, input().split()))
    k = int(input())
    threshold = int(input())
    ans = sol.numOfSubarrays(arr,k,threshold)
    print(ans)