from collections import Counter, defaultdict
class Solution:
    def exist(self, board, word: str) -> bool:
        m = len(board)
        n = len(board[0])
        w = len(word)

        if n == 1 and m == 1:
            return board[0][0] == word
            
        board_counter = defaultdict(int)
        word_counter = Counter(word)

        for i in range(m):
            for j in range(n):
                board_counter[board[i][j]] += 1

        for c in word_counter:
            if word_counter[c] > board_counter[c]:
                return False

        def backtrack(pos, index):
            i,j = pos
            if index == w:
                return True
            
            if board[i][j] != word[index]:
                return False

            char = board[i][j]
            board[i][j] = '#'

            for i_off, j_off in [(0,1), (0,-1), (1,0), (-1,0)]:
                r = i_off + i
                c = j_off + j
                if 0 <= r < m and 0 <= c < n:
                    if backtrack((r,c), index+1):
                        return True

            board[i][j] = char
            return False
            

        for i in range(m):
            for j in range(n):
                if  board[i][j] == word[0] and backtrack((i,j),0):
                    return True
        
        return False
    
#In the leetcode code editor you dont need to write the following code . It is just to run in your local machine.

if __name__ == "__main__":

    sol = Solution()
    m = int(input())
    board = []
    #Input only uppercase letters
    for _ in range(m):
        row = input().split()
        board.append(row)
    word = input()
    ans = sol.exist(board, word)
    print(ans)
        