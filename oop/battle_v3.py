import string

class Board():
    def __init__(self):
        self.size = 10
        self.board = []
        for sell in range(10):
           self.board.append(["."] * 10)

    def show(self, username, board=None):
        if board == None:
            board = self.board
        print "     USER: %s" % username
        alphabet = string.uppercase[:self.size]
        numbers = ' '.join(str(x) for x in range(1,11))
        print "     %s" % numbers
        letter = 0
        for row in range(self.size):
            board_row = " ".join(board[row])
            print "   %s %s" % (alphabet[letter],board_row)
            letter += 1

    def layout(self, ship, x, y):
        if ship.layout == 'horizontal':
            cur_x = x
            cur_y = y + 1
        if ship.layout == 'vertical':
            cur_x = x + 1
            cur_y = y
        return cur_x, cur_y

    def draw_ships(self, navy):
        for sell in range(ship.leng):
            if ship.layout == 'vertical':
                self.board[x][y + sell] = '='
            if ship.layout == 'horisontal':
                self.board[x + sell][y] = '='
            
    def selector(self, board, ship=None):
        def movement(x, y):
            exit = False
            arrow = raw_input("Move with h/j/k/l: ")
            if arrow == 'h':
                y = y - 1
            elif arrow == 'j':
                x = x + 1
            elif arrow == 'k':
                x = x - 1
            elif arrow == 'l':
                y = y + 1
            elif arrow == 'v':
                ship.layout = ship.change_layout()
            elif arrow == 'e':
                exit = True
            else:
                exit = False
            return x, y, exit

        def show_crosses(x, y):
            for loop in range(4):
                for X_x, X_y in [(-1,-1),(1,1),(-1,1),(1,-1)]:
                    try:
                        board_temp[x + X_x][y + X_y] = '+'
                    except IndexError:
                        pass

        def show_ship(x, y):
            for sell in range(ship.leng):
                if ship.layout == 'vertical':
                    board_temp[x][y+sell] = ship.body
                else:
                    board_temp[x+sell][y] = ship.body

        x = 5
        y = 5
        exit = False
        while exit == False:
            try:
                if x > 9 or y > 9 or x <= 0 or y <= 0:
                    raise IndexError
                temp_x = x
                temp_y = y
                import copy
                board_temp = copy.deepcopy(board)

                x, y, exit = movement(x,y)
                show_crosses(x, y)

                if ship:
                    show_ship(x, y)

                self.show('TEMP', board_temp)
            except IndexError:
                print('Not possible position')
                x = temp_x
                y = temp_y
                continue
        return x, y


class Ship(object):

    def __init__(self, leng):
        self.leng = leng

        # defaults
        self.body = '='
        self.damage = 'X'
        self.x = 5
        self.y = 5
        self.layout = 'horisontal' # 'vertical'

        self.ship = []
        for sell in range(self.leng):
            self.ship.append(self.body)

    def hit(self, sell):
        self.ship[sell] = self.damage 
        print self.ship
        
    def health(self):
        if self.damage not in self.ship:
            state = "Health - [ OK ]"
        elif self.damage in self.ship:
            state = "Health - [ HITed ]"
        elif self.body not in self.ship:
            state =  "Health - [ DEAD ]"
        return state

    def change_layout(self):
        if self.layout == 'horizontal':
            return 'vertical'
        else:
            return 'horizontal'

        
class Player():
    def __init__(self):
        self.name = raw_input("Enter name: ")
        print ("Hello %s" % self.name)

        self.board = Board()

        self.navy = [
         Ship(4),
         Ship(3),
         Ship(2),
         Ship(1)
        ]


    def place_ships(self):
        for ship in self.navy:
            ship.x, ship.y = self.board.selector(self.board.board, ship)
            self.board.draw_ships()


class Game():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()

    def show_gamefield(self):
        self.player1.board.show(self.player1.name)
        self.player2.board.show(self.player2.name)

    def place_ships(self):
        print "Place your ships"
        self.player1.place_ships()
        self.player2.place_ships()


if __name__ == '__main__':
    game = Game()
    game.show_gamefield()
    game.place_ships()
