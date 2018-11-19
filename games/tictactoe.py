class Board():
    def __init__(self):
        self.board = []
        for sell in range(3):
            self.board.append(['.'] * 3)

    def show(self):
        for raw in range(3):
            board_raw = ' '.join(self.board[raw])
            print("\t" + str(board_raw))

class Player():
    def __init__(self, symb, name):
        self.symb = symb
        self.name = name

    def placement(self):
        sell  = raw_input('\tEnter sell [1-9]: ')
        print("\n")
        sell = int(sell) - 1
        x = sell // 3
        y = sell % 3
        return x, y

class Game():
    def __init__(self, name1, name2):
        self.gamefield = Board()
        self.player1 = Player('X', name1)
        self.player2 = Player('0', name2)
        self.players = [self.player1,
                        self.player2]

    def turn(self):
        game_over = False
        moves = 0
        while game_over == False:
            for player in self.players:
                print("\n\tYour move, %s" % player.name)
                while True:
                    x, y = player.placement()
                    if self.gamefield.board[x][y] == '.':
                        self.gamefield.board[x][y] = player.symb
                        break
                    else:
                        print("\n\tWrong move. Try again")
                        self.gamefield.show()

                self.gamefield.show()
                game_over = self.win(player)

                if game_over:
                    break

                moves += 1
                if moves == 9:
                    print("\n\tDraft")
                    game_over = True
                    break

    def win(self, player):
        win = False
        for raw in range(3):
            if self.gamefield.board[raw][0] == player.symb and \
               self.gamefield.board[raw][1] == player.symb and \
               self.gamefield.board[raw][2] == player.symb:
                win = True
            if self.gamefield.board[0][raw] == player.symb and \
               self.gamefield.board[1][raw] == player.symb and \
               self.gamefield.board[2][raw] == player.symb:
                win = True
            if self.gamefield.board[0][0] == player.symb and \
               self.gamefield.board[1][1] == player.symb and \
               self.gamefield.board[2][2] == player.symb:
                win = True
            if self.gamefield.board[0][2] == player.symb and \
               self.gamefield.board[1][1] == player.symb and \
               self.gamefield.board[2][0] == player.symb:
                win = True
        if win:
            print("\n\t%s WINS!" % player.name)
            return True
        else:
            return False
            

if __name__ == '__main__':
    player1 = raw_input("\tPlayer X -- Enter your name: ")
    player2 = raw_input("\tPlayer 0 -- Enter your name: ")
    game = Game(str(player1),str(player2))
    game.gamefield.show()
    game.turn()
