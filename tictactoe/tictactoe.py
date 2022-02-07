import random
class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        #fills a 2d array with - which represnts open spot
        self.board = [["-" for i in range(3)] for j in range(3)]


    def print_instructions(self):
        # TODO: Print the instructions to the game
        #prints out the rules of the game
        print("Welcome to Tic Tac Toe!")
        print("Player 1 is X and Player 2 is O")
        print("Take turns placing X and Os inorder to get 3 in a row!")

    def print_board(self):
        # TODO: Print the board
        #prints out the 2d array and labels the rows and columns
        print("\t0    1    2")
        for i in range(3):
            print(i, "  " + "    ".join(self.board[i]))
            print()

    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid
        #sees if user input is out of bounds of the 2d array or if a spot is already taken
        if row > 2 or col > 2:
            return False
        if self.board[row][col] != "-":
            return False
        return True

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        #this places the player at the given row and column
            self.board[row][col] = player

    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        #Asks user for input. If the input is invalid it will ask again until input is valid
            r = int(input("Enter a row: "))
            c = int(input("Enter a column: "))
            x = bool(self.is_valid_move(r, c))
            while x is False:
                print("invalid move please try again")
                r = int(input("Enter a row: "))
                c = int(input("Enter a column: "))
                x = bool(self.is_valid_move(r, c))
            self.place_player(player, r, c)

    def take_random_turn(self, player):
        r = random.randint(0,2)
        c = random.randint(0,2)
        while self.is_valid_move(r, c) == False:
            r = random.randint(0, 2)
            c = random.randint(0, 2)
        self.place_player(player, r, c)

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        #Allows for each player to take a turn

        print("PLayer's " + player + " turn")
        if player == "X":
            self.take_manual_turn(player)
        else:
            self.take_random_turn(player)

    def check_col_win(self, player):
        # TODO: Check col win
        #sees if a player wins by have 3 in a row in a column
        colZero = 0
        colOne = 0
        colTwo = 0

        for i in range (3):
            if self.board[i][0] == player:
                colZero = colZero + 1
        if colZero == 3:
            return True

        for i in range (3):
            if self.board[i][1] == player:
                colOne = colOne + 1
        if colOne == 3:
            return True

        for i in range (3):
            if self.board[i][2] == player:
                colTwo = colTwo + 1
        if colTwo == 3:
            return True

        return False

    def check_row_win(self, player):
        # TODO: Check row win
        # sees if a player wins by have 3 in a row in a row
        rowZero = 0
        rowOne = 0
        rowTwo = 0

        for i in range(3):
            if self.board[0][i] == player:
                rowZero = rowZero + 1
        if rowZero == 3:
            return True
        for i in range(3):
            if self.board[1][i] == player:
                rowOne = rowOne + 1
        if rowOne == 3:
            return True

        for i in range(3):
            if self.board[2][i] == player:
                rowTwo = rowTwo + 1
        if rowTwo == 3:
            return True

        return False

    def check_diag_win(self, player):
        # TODO: Check diagonal win
        # sees if a player wins by have 3 in a row in a diagonal line
        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True

        if self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player:
            return True
        return False

    def check_win(self, player):
        # TODO: Check win
        #uses the last 3 methods to see if a user won in any direction
        if self.check_row_win(player) == True or self.check_col_win(player) == True or self.check_diag_win(player) == True:
            return True
        return False

    def check_tie(self):
        # TODO: Check tie
        #Checks to see if there are no more spaces left
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "-":
                    return False
        return True

    def change_player(self, player):
        # This switches who's turn it is
        if player == "X":
            return "O"
        if player == "O":
            return "X"

    def play_game(self):
        # TODO: Play game
        #uses all the methods up above to run the game untill a tie or a winner
        self.print_instructions()
        self.print_board()
        play = True
        player = "O"
        while play:
            player = self.change_player(player)
            self.take_turn(player)
            self.print_board()
            if self.check_win(player):
                print("Player " + player + " won!")
                play = False
            if self.check_tie():
                print("Tie")
                play = False


