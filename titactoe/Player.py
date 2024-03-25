import random
class Player():
    def __init__(self, isHuman=True, marker='X') -> None:
        self.isHuman = isHuman
        # ensure marker is capitalized and defaults to 'X' or 'O' correctly
        self.marker = 'X' if marker.upper() == 'X' else 'O'

    def getMarker(self):
        return self.marker
    
    def getIsHuman(self):
        return self.isHuman
    
    def getHumanMove(self, board):
        while True:
            user_move = input(f"Player Move ({self.marker}: )")
            if board.isMoveValid(user_move):
                return user_move
            else: 
                print('Invalid Input: Please enter the column and row of your move (Example:)')
    
    def generateComputerMove(self, board):
        possible_move = [f"{chr(col + ord('A'))}{row + 1}" for col in range(board.boardSize) for row in range(board.boardSize) if board.gameBoard[row][col] == ' ']
        return random.choice(possible_move)
    
    def getPlayerMove(self, board):
        return self.getHumanMove(board) if self.isHuman else self.generateComputerMove(board)
    
