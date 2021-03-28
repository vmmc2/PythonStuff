class Solver:
    def __init__(self, board):
        self.board = board
        self.valid = None 

    def getValid(self):
        return self.valid 

    def isXWinner(self):
        # Checando se X foi vencedor:
        if self.board[0] == ['X', 'X', 'X'] or self.board[1] == ['X', 'X', 'X'] or self.board[2] == ['X', 'X', 'X']:
            return True
        if (self.board[0][0] == 'X' and self.board[1][0] == 'X' and self.board[2][0] == 'X') or (self.board[0][1] == 'X' and self.board[1][1] == 'X' and self.board[2][1] == 'X') or (self.board[0][2] == 'X' and self.board[1][2] == 'X' and self.board[2][2] == 'X'):
            return True
        if (self.board[0][0] == 'X' and self.board[1][1] == 'X' and self.board[2][2] == 'X') or (self.board[0][2] == 'X' and self.board[1][1] == 'X' and self.board[2][0] == 'X'):
            return True
        return False
        
    def isOWinner(self):
        # Checando se O foi vencedor:
        if self.board[0] == ['O', 'O', 'O'] or self.board[1] == ['O', 'O', 'O'] or self.board[2] == ['O', 'O', 'O']:
            return True
        if (self.board[0][0] == 'O' and self.board[1][0] == 'O' and self.board[2][0] == 'O') or (self.board[0][1] == 'O' and self.board[1][1] == 'O' and self.board[2][1] == 'O') or (self.board[0][2] == 'O' and self.board[1][2] == 'O' and self.board[2][2] == 'O'):
            return True 
        if (self.board[0][0] == 'O' and self.board[1][1] == 'O' and self.board[2][2] == 'O') or (self.board[0][2] == 'O' and self.board[1][1] == 'O' and self.board[2][0] == 'O'):
            return True
        return False

    def checkValid(self):
        # Um tabuleiro eh ilegal se tiver dois vencedores simultaneos ou se tiver mais jogadas de 'O' do que de 'X'.
        xWinner = None
        oWinner = None 
        numO = 0
        numX = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == 'O':
                    numO += 1
                elif self.board[i][j] == 'X':
                    numX += 1
        if (numX == numO) or (numX == numO + 1):
            if self.isOWinner() == True:
                if self.isXWinner() == True:
                    self.valid = False
                    return
                if numO == numX:
                    self.valid = True 
                    return
                else:
                    self.valid = False
                    return
            if self.isXWinner() == True and (numX != numO + 1):
                self.valid = False 
                return
            self.valid = True 
            return    
        else:
            self.valid = False
        return


def main():
    n = int(input())
    for i in range(0, n):
        l1 = input().split()
        l2 = input().split()
        l3 = input().split()
        board = [l1, l2, l3]
        s = Solver(board)
        s.checkValid()
        if s.getValid() == False:
            print("ILEGAL")
        else:
            if s.isOWinner() == True:
                print("O_VENCEU")
            elif s.isXWinner() == True:
                print("X_VENCEU")
            else:
                print("EM_ANDAMENTO")
    return

if __name__ == "__main__":
    main()
