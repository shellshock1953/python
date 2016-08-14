"""
    make shots like A1, C4
    make up to three diferent types to sheeps - 1, 2, 3 sells
    random it horizontally or vertically
    dont allow be closer then one sell between sheeps
    make user to set ships
    make bot player (more agresive)
    
    ask to randomize ship placement
    make singleplayer game
    show two boards
    boards 10x10 -- make biger resolution, 1 sell is 4 ascii?
    screen refresh, colorize
    bot answers in zy***-style
    vizual effects? (splash, logo, hit, fire...)
    music? (lol)
    
    far future
    board 20x20 -- ship movement - one turn, move or shot
"""
import random

def board_generator(size):
    board = []
    for sell in range(size):
        board.append(["."] * size)
    return board

def board_show(player_board,bot_board):
    print "  1 2 3 4 5 6 7 8 9 10     1 2 3 4 5 6 7 8 9 10"
    abc = "abcdefghij"
    i = 0
    for row in range(len(board[0])):
        player_row = " ".join(player_board[row])
        bot_row = " ".join(bot_board[row])
        # print abc[i]," ".join(player_board[row])
        print ("%s %s    %s %s") % (abc[i], player_row, abc[i], bot_row)
        i += 1

def get_coordinates():
    while True:
        alph_coordinate = raw_input("Enter coordinates:")
        x_alph = alph_coordinate[0]
        y_alph = alph_coordinate[1]
        if x_alph in "abcdefghij" and str(y_alph) in str(range(1,11)):
            return alph_coordinate
        else:
            print "Wrong coordinates!"

def coordinate_convertor(alph_coordinate):
    x_alph = alph_coordinate[0]
    y_alph = alph_coordinate[1:]
    coordinate_dict = {
        "a":1,
        "b":2,
        "c":3,
        "d":4,
        "e":5,
        "f":6,
        "g":7,
        "h":8,
        "i":9,
        "j":10,
    }
    x = coordinate_dict[x_alph] - 1
    y = int(y_alph) - 1
    return(x,y)

def shoots(alph_coordinate,board):
    x, y = coordinate_convertor(alph_coordinate)
    if board[int(x)][int(y)] == "~":
        print "already shot this place!"
    if board[int(x)][int(y)] == "=":
        print "HIT!"
        board[int(x)][int(y)] = "x"
    else:
        board[int(x)][int(y)] = "~"
        return board

def place_ship(x, y, ship_len, orientation, board):
    for sell in range(int(ship_len)):
        if orientation == "hor":
            board[int(x)][int(y) + sell] = "="
        elif orientation == "ver":
            board[x + sell][y] = "="
        else:
            print "Wrong orientation"
    return board

def place_ship_error_check(x, y, ship_len, board):
    if int(x) + int(ship_len) > 10 or \
       int(y) + int(ship_len) > 10 :
        print "out of the board"
        has_errors = True
    elif board[x][y] == "=":
        print "cant place ship above another one"
        has_errors = True
    else:
        has_errors = False
    return has_errors

def manual_place_ship():
    print "Place thee ships on a board"
    for i in range(1,2):
        print "Ship No:", i
        has_errors = True
        while has_errors == True:
            alph_coordinate = raw_input("Enter alph coordinate: ")
            x, y = coordinate_convertor(alph_coordinate)
            ship_len = raw_input("Enter ship_len: ")
            orientation = raw_input("Eneter orientation 'hor/ver': ")
            has_errors = place_ship_error_check(x, y, ship_len)
        place_ship(x, y, ship_len, orientation, board)
        board_show(board)
        i += 1
        print ""

def random_place_ship(board):
    for i in range(1,4):
        has_errors = True
        while has_errors == True:
            x = random.randint(0,10)
            y = random.randint(0,10)
            ship_len = random.randint(1,5)
            orientation = random.choice(["hor","ver"])
            print x, y, ship_len, orientation
            has_errors = place_ship_error_check(x, y, ship_len,board)
        place_ship(x, y, ship_len, orientation, board)
        i += 1

def bot():
    alph = "abcdefghij"
    num  = range(10)
    bot_shot = alph[random.randint(0,10)] + str(num[random.randint(0,10)])
    print bot_shot
    shoots(bot_shot,board)

def game_over(player_board, bot_board):
    for row in range(len(board[0])):
        if "=" not in player_board[row]:
            print "YOU LOSE!"
        if "=" not in bot_board[row]:
            print "YOU WIN!"

if __name__ == "__main__":
    board = board_generator(10)
    bot_board = board_generator(10)
    random_place_ship(board)
    random_place_ship(bot_board)
    board_show(board,bot_board)
    while True:
        bot()
        alph_coordinate = get_coordinates()
        shoots(alph_coordinate,bot_board)
        board_show(board,bot_board)
        game_over(board, bot_board)

