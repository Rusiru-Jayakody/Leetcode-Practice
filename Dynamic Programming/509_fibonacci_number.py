#top down approach(Memoization- using DP)
class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1}

        def fib(n):
            if n in memo:
                return memo[n]
            memo[n] = fib(n-1) + fib(n-2)
            return memo[n]
        return fib(n)

#Bottom up aproch using tabulation    
# class Solution:
#     def fib(self, n: int) -> int:
#         dp = [0] * (n+1)
#         dp[0] = 0
#         if n > 0:
#             dp[1] = 1

#         for i in range(2,n+1):
#             dp[i] = dp[i-1] + dp[i-2]
        
#         return dp[n]


#CONSTANT SPACE SOLUTION
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1

#         prev = 0
#         curr = 1
        
#         for _ in range(2,n+1):
#             prev , curr = curr, prev + curr
        
#         return curr
        
        

#Naive recursive solution (not efficient)
# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         return self.fib(n-1) + self.fib(n-2)


#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":
    sol = Solution()
    n = int(input())
    ans = sol.fib(n)
    print(ans)
        