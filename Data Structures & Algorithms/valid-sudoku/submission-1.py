class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in range(9):
            includes = set()
            includes.clear()
            for col in range(9):
                if board[row][col] in includes and board[row][col].isnumeric():
                    return False
                else:
                    includes.add(board[row][col])

        for col in range(9):
            includes = set()
            includes.clear()
            for row in range(9):
                if board[row][col] in includes and board[row][col].isnumeric():
                    return False
                else:
                    includes.add(board[row][col])

        dictVals = {}

        for row in range(9):
            for col in range(9):   
                location = (row//3)*10 + (col//3)
                if location in dictVals and board[row][col] in dictVals[location] and board[row][col].isnumeric():
                    return False
                elif location in dictVals:
                    dictVals[location].append(board[row][col])
                else:
                    dictVals[location] = [board[row][col]]



        return True
