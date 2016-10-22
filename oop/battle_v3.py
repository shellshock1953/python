import string



class Board():
    board = []
    size = 10
    
    def generate(self):
        for sell in range(10):
           self.board.append(["."] * 10)
        return self.board

    def refresh(self):
        print self.navy['2sell_a'].health()
        print self.navy['2sell_a'].ship

    def show(self):
        alphabet = string.uppercase[:self.size]
        numbers = ' '.join(str(x) for x in range(1,11))
        print "     %s" % numbers
        letter = 0
        for row in range(self.size):
            board_row = " ".join(self.board[row])
            print "   %s %s" % (alphabet[letter],board_row)
            letter += 1
            

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
        

class Player(Board, Ship):
    def __init__(self, name):
        self.name = name
        print ("Hello %s" % name)

    navy = {
        '4sell_a' : Ship(1,1,4,'vertical'),
        '2sell_a' : Ship(3,1,2,'horisontal'),
        '2sell_b' : Ship(5,1,2,'horisontal'),
    }

if __name__ == '__main__':
    player = Player('shellshock')
    player.generate()
    player.navy['2sell_a'].hit(0)
    player.navy['2sell_a'].hit(1)
    player.show()
    player.refresh()
