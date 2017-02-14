class Board():
    def __init__(self):
        var1 = raw_input("Enter Value:")
        self.var1 = var1

class Player():
    def __init__(self):
        name = raw_input("Enter Name:")
        board = Board()
        self.var = board.var1
        self.name = name
    def show(self):
        print self.name + " " + self.var

player1 = Player()
player2 = Player()
player1.show()
player2.show()
