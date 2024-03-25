class TTTBoard():
    def __init__(self, boardSize) -> None:
        self.boardSize = boardSize
        # create a board with n*n matrix
        self.gameBoard = {str(num):' ' for num in range(boardSize ** 2)}
        
    def getGameBoard(self):
        # print the column headers
        column = "  " + " ".join(chr(ord('A') + i) for i in range(self.boardSize))
        print(column)
        for row in range(1, self.boardSize + 1):
            cells = ' |' * self.boardSize
            print(f"{row}{cells} ")
            if row < self.boardSize:
                print(" " + "-"*(self.boardSize * 2 + 1))

    def printBoard(self):
        column = " " + " ".join(str(i + 1) for i in range(self.boardSize))
        print(column)
        for row in range(1, self.boardSize + 1):
            cells = ' |' * self.boardSize
            print(f'{row}{cells}')
            print("-" * (self.boardSize*2 + 1))

    def isMoveValid(self, move):
        if len(move) != 2:
            return False
        # A, B, C ....
        col = move[0].upper()
        # Row numbers 1, 2, 3
        row = move[1]
        if col < 'A' or col > 'C' or not row.isdigit():
            return False
        row = int(row) - 1
        col = ord(col) - ord('A')
        return 0 <= row < self.boardSize and 0 <= col < self.boardSize
        


    def submitMove(self, move, player):
        # adds the move the board, and returns true if the space is not taken
        # return false and not add the move
        # The ord function takes a single Unicode character (string of length 1) and returns its integer Unicode code point.
        col = ord(move[0].upper()) - ord('A')
        # Convert move from format 'A1' to board index '0', '1', ...
        row = int(move[1]) - 1
        """
        If your dictionary's keys are linear indices ('0', '1', ..., representing cells in a row-major order), 
        you convert the 2D row and col indices to a single linear index. Given row and col, 
        the linear index index for an n x n board is calculated as index = row * n + col, where n is the board size (number of columns/rows).
        """
        index = row * self.boardSize + col

        if  self.isMoveValid(move) and (self.gameBoard[index] == ' '):
            self.gameBoard[index] = player
            return True
        else:
            return False

    def isWinner(self, player):
        # Check rows
        for row in range(self.boardSize):
            if all(self.gameBoard[str(row * self.boardSize + col)] == player for col in range(self.boardSize)):
                return True
                
        # Check columns
        for col in range(self.boardSize):
            if all(self.gameBoard[str(row * self.boardSize + col)] == player for row in range(self.boardSize)):
                return True
                
        # Check diagonal (top-left to bottom-right)
        if all(self.gameBoard[str(i * self.boardSize + i)] == player for i in range(self.boardSize)):
            return True
            
        # Check anti-diagonal (top-right to bottom-left)
        if all(self.gameBoard[str(i * self.boardSize + (self.boardSize - 1 - i))] == player for i in range(self.boardSize)):
            return True
            
        return False




        

        