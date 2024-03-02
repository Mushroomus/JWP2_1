class TicTacToe:
    ALL_SPACES = list('123456789')
    X, O, BLANK = 'X', 'O', ' '

    def __init__(self):
        self.game_board = self.get_blank_board()
        self.current_player = self.X

    def get_blank_board(self):
        board = {}
        for space in self.ALL_SPACES:
            board[space] = self.BLANK
        return board

    def get_board_str(self):
        board = self.game_board
        return f'''
                {board['1']}|{board['2']}|{board['3']} 1 2 3 
                -+-+- 
                {board['4']}|{board['5']}|{board['6']} 4 5 6 
                -+-+- 
                {board['7']}|{board['8']}|{board['9']} 7 8 9'''

    def is_valid_space(self, space):
        if space is None:
            return False
        return space in self.ALL_SPACES or self.game_board[space] == self.BLANK

    def is_winner(self, player):
        b, p = self.game_board, player
        return ((b['1'] == b['2'] == b['3'] == p) or
                (b['4'] == b['5'] == b['6'] == p) or
                (b['7'] == b['8'] == b['9'] == p) or
                (b['1'] == b['4'] == b['7'] == p) or
                (b['2'] == b['5'] == b['8'] == p) or
                (b['3'] == b['6'] == b['9'] == p) or
                (b['3'] == b['5'] == b['7'] == p) or
                (b['1'] == b['5'] == b['9'] == p))

    def is_board_full(self):
        for space in self.ALL_SPACES:
            if self.game_board[space] == self.BLANK:
                return False
        return True

    def update_board(self, space, mark):
        self.game_board[space] = mark

    def switch_player(self):
        self.current_player = self.O if self.current_player == self.X else self.X

    def play_game(self):
        print('Welcome to Tic Tac Toe!')
        while True:
            print(self.get_board_str())

            move = None
            while not self.is_valid_space(move):
                print(f'Player {self.current_player}, what is your move? (1-9)')
                move = input()

            self.update_board(move, self.current_player)

            if self.is_winner(self.current_player):
                print(self.get_board_str())
                print(f'Player {self.current_player} wins!')
                break
            elif self.is_board_full():
                print(self.get_board_str())
                print('The game ended in a tie!')
                break

            self.switch_player()

        print('Thanks for playing!')


if __name__ == '__main__':
    game = TicTacToe()
    game.play_game()
