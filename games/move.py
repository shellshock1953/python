# todo rotate self.game_over
# todo dont press enter
# todo more beautiful board
# todo correct clear screen


from random import shuffle
import os

class Board():
    def __init__(self):
        self.empty_char = '■'
        self.board = list()
        self.game_over = list()
        self.generate_random()
        self.generate_game_over()
        self.x, self.y = self.find_start_point()

    def generate_random(self):
        num_list = [str(i) for i in range(1, 9)]
        num_list.append(self.empty_char)
        shuffle(num_list)
        self.board = [num_list[i::3] for i in range(3)]

    def generate_game_over(self):
        num_list = [str(i) for i in range(1, 9)]
        num_list.append(self.empty_char)
        self.game_over = [num_list[i::3] for i in range(3)]

    def show(self):
        # os.system('clear')
        print('\n' * 100)
        print('+ -  -  - +')
        for row in range(3):
            str_row = "  ".join(self.board[row])
            print("| {} |".format(str_row))
        print('+ -  -  - +')

    def find_start_point(self):
        for row in range(3):
            if self.empty_char in self.board[row]:
                x = row
                y = self.board[row].index(self.empty_char)
                return x, y

    def movement(self, x, y):
        rX = x
        rY = y
        arrow = input(">_ enter move: ")

        if   arrow == '1': y = y - 1
        elif arrow == '2': x = x + 1
        elif arrow == '5': x = x - 1
        elif arrow == '3': y = y + 1
        if x < 0 or y < 0:
            raise IndexError
        save_num = self.board[x][y]
        self.board[x][y] = self.empty_char
        self.board[rX][rY] = save_num
        return x, y

    def game(self):
        while True:
            try:
                self.show()
                self.x, self.y = self.movement(self.x, self.y)
            except IndexError:
                self.show()
                print('>_ illegal move')
                continue
            if self.board == self.game_over:
                self.show()
                print('>_ U Win   !')
                print('>_ Congrats!')
                exit(0)



if __name__ == '__main__':
    game = Board()
    game.game()
