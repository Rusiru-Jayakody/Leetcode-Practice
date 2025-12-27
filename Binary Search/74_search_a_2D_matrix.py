class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, (m*n)-1
        while l <= r:
            mid = l + (r-l)//2
            i = mid//n
            j = mid % n
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    m,n = map(int, input().split())
    matrix = []
    for _ in range(m):
        matrix.append(list(map(int, input().split())))
    target = int(input())
    ans = sol.searchMatrix(matrix, target)
    print(ans)
        


        

            
