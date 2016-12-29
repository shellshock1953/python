import string

class Board():
    def __init__(self):
        self.size = 10
        self.board = []
        for sell in range(10):
           self.board.append(["."] * 10)

    def show(self, username):
        print "     USER: %s" % username
        alphabet = string.uppercase[:self.size]
        numbers = ' '.join(str(x) for x in range(1,11))
        print "     %s" % numbers
        letter = 0
        for row in range(self.size):
            board_row = " ".join(self.board[row])
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
        for ship in navy.values():
            x = ship.x
            y = ship.y
            leng = ship.leng
            layout = ship.layout
            for sell in range(leng):
                if ship.layout == 'vertical':
                    self.board[x][y + sell] = '='
                if ship.layout == 'horisontal':
                    self.board[x + sell][y] = '='
            
    def place_ships(self, navy):

class Ship():
    body = '='
    damage = 'X'

    def __init__(self, x, y, leng, layout):
        self.x = x
        self.y = y
        self.leng = leng
        self.layout = layout

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

        
class Player():
    def __init__(self):
        self.name = raw_input("Enter name: ")
        print ("Hello %s" % self.name)

        self.board = Board()

    navy = {
        '4sell_a' : Ship(1,1,4,'vertical'),
        '2sell_a' : Ship(3,1,2,'horisontal'),
        # '2sell_b' : Ship(5,1,2,'horisontal'),
    }

    def draw_ships(self):
        self.board.draw_ships(self.navy)


class Game():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.player1.draw_ships()

    def show_gamefield(self):
        self.player1.board.show(self.player1.name)
        self.player2.board.show(self.player2.name)


if __name__ == '__main__':
    game = Game()
    game.show_gamefield()
