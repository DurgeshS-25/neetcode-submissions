class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = {r:set() for r in range(9)}
        col = {c:set() for c in range(9)}
        square = {(r,c): set() for r in range(3) for c in range(3)}



        for r in range(9):
            for c in range(9):
                if board[r][c]  == '.':
                    continue

                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3,c//3)]:
                    return False

                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])

        return True

                


        