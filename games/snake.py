import time
import copy
import sys, select
import os
import random

class Board():
    def __init__(self, size=10):
        self.size = size
        self.board = self.generate()
    
    def generate(self):
        board = [[ '.' for _ in range(self.size)] for _ in range(self.size)]
        return board

    def show(self, snake=None):
        os.system('clear')
        board = copy.deepcopy(self.board)
        if snake:
            for snake_sell in snake:
                y, x = snake_sell
                board[y][x] = 'x'
        for row in range(self.size):
            str_row = " ".join(board[row])
            print " %s " % (str_row)

class Snake():
    def __init__(self, len=7, vector='right'):
        self.len = len
        self.vector = vector
        self.body = []
        self.first_gen()

    def vector_to_num(self, y, x):
        _y, _x = 0, 0
        if self.vector == 'up': _y, _x = 1, 0
        elif self.vector == 'down': _y, _x = -1, 0 
        elif self.vector == 'left': _y, _x = 0, -1 
        elif self.vector == 'right': _y, _x = 0, 1 
        y = y + _y
        x = x + _x
        return y, x

    def first_gen(self):
        y, x = 5, 5  # starting
        self.body.append((y, x)) # aka tail
        for sell in range(self.len):
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
    def __init__(self, sleep=1.0):
        self.board = Board()
        self.snake = Snake()
        self.hello()
        self.board.show(self.snake.body)
        self.game_over = False
        self.sleep = sleep/2
        self.donut = None
        self.donut_lives = 5
        self.donul_sleep = 5
    
    def hello(self):
        os.system('clear')
        print("")
        print("=== HELLO IN SNAKE: THE GAME ===")
        print("")
        print(" 1) try to get donuts shown as '0'")
        print(" 2) dont eat yourself")
        print(" 3) move like VIM hjkl")
        print("")
        select.select( [sys.stdin], [], [], 5)

    def run(self):
        while not self.game_over:
            self.board.show(self.snake.body)
            self.input()
            self.snake.step()
            self.check_game_over()
            time.sleep(self.sleep)
    
    def input(self):
        print("Move with hjkl")
        i, o, e = select.select( [sys.stdin], [], [], self.sleep )
        if (i):
            arrow = sys.stdin.readline().strip()
            if arrow not in ['h', 'j', 'k', 'l']:
                print('cant understand, executing automove')
            else:
                if arrow == 'h' and self.snake.vector != 'right': self.snake.vector = 'left'
                elif arrow == 'k' and self.snake.vector != 'up': self.snake.vector = 'down'
                elif arrow == 'j' and self.snake.vector != 'down': self.snake.vector = 'up'
                elif arrow == 'l' and self.snake.vector != 'left': self.snake.vector = 'right'
        else:
            print('nothing selected, automove')

    def donut(self):
        if self.donut_sleep != 0:
            self.donut_sleep -= 1
        else:
            rand_wrong = True
            while rand_wrong:
                y = random.randint(0,9)
                x = random.randint(0,9)
                if (x, y) in self.snake.body:
                    continue
                else:
                    self.donut = (x, y)
                    rand_wrong = False


    def check_game_over(self):
        uniq = []
        for sell in range(self.snake.len):
            if self.snake.body[sell] not in uniq:
                uniq.append(self.snake.body[sell])
            else:
                print("")
                print("")
                print("=== Game Over ===")
                self.game_over = True
                break


if __name__ == '__main__':
    game = Game()
    game.run()


