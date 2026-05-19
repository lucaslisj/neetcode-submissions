class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for col in range(9):
            seen = set()
            for i in range(9):
                if board[col][i] == '.':
                    continue
                if board[col][i] in seen:
                    return False
                else:
                    seen.add(board[col][i])
        
        # col
        for row in range(9):
            seen = set()
            for i in range(9):
                if board[i][row] == '.':
                    continue 
                if board[i][row] in seen:
                    return False
                else:
                    seen.add(board[i][row])
        
        # 3x3
        for col in range(0,9,3):
            cur_col = col
            for row in range(0,9,3):
                cur_row = row
                seen = set()
                for i in range(cur_col,cur_col+3):
                    for j in range(cur_row,cur_row+3):
                        if board[i][j] == '.':
                            continue
                        elif board[i][j] in seen:
                            return False
                        else:
                            seen.add(board[i][j])
        return True
