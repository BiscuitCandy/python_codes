import random

# the board
class TicTacToe_Board :
    
    def __init__(self) :
        self.board = [["##" for j in range(1, 4)]for i in range(1, 4)]


    def isEmpty(self, value):
        return not value in ["X", "0"]


    def Empty_places(self) :
        empty = []
        for i in self.board :
            for j in i:
                if self.isEmpty(j):
                    empty.append((self.board.index(i)+1, i.index(j)+1))
        return empty


    def diagonalpass(self) :
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] in ["X", "0"] :
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] in ["X", "0"] :
            return self.board[0][2]
        return False
    

    def columnpass(self) :

        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] and self.board[0][i] in ["X", "0"]:
                return self.board[0][i]
        return False


    def checkWinner(self) :
        
        if ["X", "X", "X"] in self.board :
            return "X"

        elif ["0", "0", "0"] in self.board :
            return "0"

        elif (winner := self.columnpass()) :
            return winner
        
        elif (winner := self.diagonalpass()):
            return winner
        
        else:
            return False
        

    def display_board(self) :

        for i in range(3):
            print("+"*18)
            print(("|"+(" "*4)+"|")*3)
            for j in range(3):
                print("|" + str(self.board[i][j]).center(4) + "|", end = "")
            print("**", i+1 , "**" )
            print(("|"+(" "*4)+"|")*3)
        print("+"*18)


    def GameOver(self) :
        return  self.Empty_places() == []
        



#Player 1
class player :

    def __init__(self, player_symbol, board):
        self.player_symbol = player_symbol
        self.board = board

    def choose(self, Empty_place) :
        x, y = Empty_place
        self.board.board[x-1][y-1] = self.player_symbol



#Player 2
class ComputerPlayer(player) :

    def __init__(self, player_symbol, board):
        super().__init__(player_symbol, board)

    def choose(self) :
        x, y = random.choice(self.board.Empty_places())
        self.board.board[x-1][y-1] = self.player_symbol

    

if __name__ == "__main__":
    
    board = TicTacToe_Board()
    board.display_board()
    player1_symbol = random.choice(["X", "0"])
    player2_symbol = "0" if player1_symbol == "X" else "X"
    print("-//-"*5)
    print("Lets Start the Game")
    print("PLAYER1 SYMBOL -", player1_symbol)
    print("PLAYER2 SYMBOL -", player2_symbol)
    print("Player1 is the human player")
    print("Player2 is the Computer player (Not AI)")
    print("-//-"*5)
    player1 = player(player1_symbol, board)
    player2 = ComputerPlayer(player2_symbol, board)
    start_turn = random.randrange(2, 5)
    start_turn_player = "Player1" if start_turn%2 else "Player2"
    print(start_turn_player, "won the TOSS, And gets to choose FIRST")
    print("Firstly, it's", start_turn_player, "turn")
    turn = 0
    while not (board.GameOver() or board.checkWinner()) and turn < 9:
        turn += 1
        print("TURN -", turn)
        if start_turn_player == "Player1" and turn % 2:
            print("It's Player1's turn")
            r_n = int(input("Enter Row Number"))
            c_n = int(input("Enter Column Number"))
            if r_n in [1, 2, 3] and c_n in [1, 2, 3]:
                player1.choose((r_n, c_n))
            else:
                print("Given INVALID row and column numbers")
                turn -= 1
        elif start_turn_player == "Player1" and turn % 2 == 0:
            print("It's Player2's turn")
            player2.choose()
        elif start_turn_player == "Player2" and turn % 2 == 0:
            print("It's Player1's turn")
            r_n = int(input("Enter Row Number"))
            c_n = int(input("Enter Column Number"))
            if r_n in [1, 2, 3] and c_n in [1, 2, 3]:
                player1.choose((r_n, c_n))
            else:
                print("Given INVALID row and column numbers")
                turn -= 1
        elif start_turn_player == "Player2" and turn % 2:
            print("It's Player2's turn")
            player2.choose()
        board.display_board()
        if board.checkWinner() :
            print("The Winner is", "Player1" if board.checkWinner() == player1_symbol else "Player2")
        elif board.GameOver():
            print("It's a tie")
