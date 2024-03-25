from TicTacToeBoard import TicTacToeBoard
from Player import Player

def main():
    print("***********")
    print("Tic-Tac-Toe")
    print("***********")

    board = TicTacToeBoard(3)
    player1 = Player(isHuman=True, marker='X')
    player2 = Player(isHuman=True, marker='O')
    current_player = player1
    while True:
        board.printBoard()
        move = current_player.getPlayerMove(board)
        if board.submitMove(move, current_player.getMarker()):
            if board.isWinner(current_player.getMarker()):
                board.printBoard()
                print(f"Player {current_player.getMarker()} wins")
                break
            elif board.isCat():
                board.printBoard()
                print("The game is a tie!")
                break

            # Switch players
            current_player = player2 if current_player == player1 else player1
        else:
            print("The space entered is already taken.")

if __name__ == "__main__":
    main()




