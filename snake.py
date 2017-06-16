class Board():
    def __init__(self, size=10):
        self.size = size
        self.board = self.generate()
    
    def generate(self):
        board = [[ '.' for _ in range(self.size)] for _ in range(self.size)]
        return board

    def show(self, snake=None):
        if snake:
            for snake_sell in snake:
                y, x = snake_sell
                self.board[y][x] = 'x'
        for row in range(self.size):
            str_row = " ".join(self.board[row])
            print " %s " % (str_row)

class Snake():
    def __init__(self, len=3, vector='right'):
        self.len = len
        self.vector = vector
        self.body = []
        self.first_gen()

    def vector_to_num(self, y, x):
        _y, _x = 0, 0
        if self.vector == 'up':
            _y, _x = 1, 0
        elif self.vector == 'down':
            _y, _x = -1, 0 
        elif self.vector == 'left':
            _y, _x = 0, -1 
        elif self.vector == 'right':
            _y, _x = 0, 1 
        y = y + _y
        x = x + _x
        return y, x

    def first_gen(self):
        y, x = 5, 5  # starting
        self.body.append((y, x)) # aka tail
        for sell in range(self.len):
            #import pdb; pdb.set_trace()
            y, x = self.vector_to_num(y, x)
            y, x = self.mod(y, x)
            self.body.append((y, x))
    
    def step(self):
        self.body.pop(0)  # rm tail
        head = len(self.body) - 1
        y, x = self.body[head]
        y, x = self.vector_to_num(y, x)
        y, x = self.mod(y, x)
        self.body.append((y, x))

    def mod(self, y, x):
        y = y%9
        x = x%9
        return y, x
        
class Game():
    def __init__(self):
        self.board = Board()
        self.snake = Snake()
        self.board.show(self.snake.body)
        self.game_over = False

    def run():
        while not self.game_over:


if __name__ == '__main__':
    game = Game()
    print game.snake.body


