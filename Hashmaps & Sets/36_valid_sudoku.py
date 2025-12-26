class Solution:
    def isValidSudoku(self, board) -> bool:
        
        for row in board:
            sett1 = set()
            for c in row:
                if c == ".":
                    continue
                elif c in sett1:
                    return False
                sett1.add(c)

        for i in range(9):
            sett2 = set()
            for j in range(9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in sett2:
                    return False
                sett2.add(board[j][i])
        
        r, c = 0,0
        for k in range(9):
            sett3 = set()
            if k % 3 == 0:
                c = 0
                r = k
            for i in range(3):
                for j in range(3):
                    if board[i+r][j+c] == ".":
                        continue
                    elif board[i+r][j+c] in sett3:
                        return False
                    sett3.add(board[i+r][j+c])
            c += 3
            
        
        return True
            

#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    board = []
    for i in range(9):
        row = input().split()
        board.append(row)
    ans = sol.isValidSudoku(board)
    print(ans)           

        