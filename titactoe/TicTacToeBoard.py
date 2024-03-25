class TicTacToeBoard():
    def __init__(self, size) -> None:
        self.gameBoard = [[' ' for _ in range(size)] for _ in range(size)]
        self.boardSize = size

    def getGameBoard(self):
        return self.gameBoard



    def printBoard(self):
        column_headers = "  " + " ".join(chr(ord('A') + i) for i in range(self.boardSize))
        print(column_headers)
        for row in range(self.boardSize):
            row_display = str(row + 1) + " " + " | ".join(self.gameBoard[row])
            print(row_display)
            if row < self.boardSize - 1:
                print("  " + "-" * (self.boardSize * 4 - 1))
    
    def isMoveValid(self, move):
        if len(move) != 2:
            return False
        col = move[0].upper()
        row = move[1]
        if col < 'A' or col > chr(ord('A') + self.boardSize - 1) or not row.isdigit():
            return False
        row = int(row) - 1
        col = ord(col) - ord('A')
        return 0 <= row < self.boardSize and 0 <= col < self.boardSize and self.gameBoard[row][col] == ' '

    
    def submitMove(self, move, player):
        col = ord(move[0].upper()) - ord('A')
        row = int(move[1]) - 1
        if self.isMoveValid(move) and self.gameBoard[row][col] == ' ':
            self.gameBoard[row][col] = player
            return True
        return False
    
    def isWinner(self, player):
        # check for rows and columns 
        for i in range(self.boardSize):
            if all(self.gameBoard[i][j] == player for j in range(self.boardSize)) or all(self.gameBoard[j][i] == player for j in range(3)):
                return True
        # check for diagnoals
        if all(self.gameBoard[i][i] == player for i in range(self.boardSize)) or all(self.gameBoard[i][self.boardSize - 1 -i] == player for i in range(self.boardSize)):
            return True
        return False

    # Return true if there is a CAT(tie), false otherwise
    def isCat(self):
        for row in self.gameBoard:
            if ' ' in row:
                return False
        return not self.isWinner('X') and not self.isWinner('O')