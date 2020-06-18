class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid = True
        # First Step: Check each line.
        freq = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        for i in range(0, 9):
            # traversing through all cells of a row.
            freq = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
            for j in range(0, 9):
                if board[i][j] == '.': continue
                else:
                    freq[board[i][j]] += 1
                    if freq[board[i][j]] > 1:
                        valid = False
        if valid == False:
            return valid
        
        # Second step: Check each column.
        for j in range(0, 9):
            # traversing through all cells of a column.
            freq = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
            for i in range(0, 9):
                if board[i][j] == '.': continue
                else:
                    freq[board[i][j]] += 1
                    if freq[board[i][j]] > 1:
                        valid = False
        if valid == False:
            return valid
        
        # Third Step: Check each sub-square
        i = 0
        j = 0
        a = 0
        b = 0
        while i <=6:
            j = 0
            while j <= 6:
                a = 0
                b = 0
                freq = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
                for a in range(0, 3):
                    for b in range(0, 3):
                        if board[i + a][j + b] == '.': continue
                        else:
                            freq[board[i + a][j + b]] += 1
                            if freq[board[i + a][j + b]] > 1:
                                valid = False
                j += 3
            i += 3
        return valid
                
