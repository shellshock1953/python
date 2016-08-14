"""second try
defs
    generate_board
    random_ship_placement
        check_ships_placement
    show_boards
    show_messages
    shots
    hits
    bot_logic
        bot_hit
"""
import string
import random
# ACT 1. Game field


def generate_board(board_size):
    board = []
    for sell in range(board_size):
        board.append(["."] * board_size)
    return board


def show_head():
    print("     PLAYER\t\t\t  BOT")


def show_boards(player_board, bot_board, board_size):
    """ TODO: make tabulate if board size bigger than 10"""
    numbers = ' '.join(str(x) for x in range(1, board_size + 1))
    print("     %s\t  %s") % (numbers, numbers)
    alphabet = string.uppercase
    alphabet = alphabet[:board_size]
    letter = 0
    for row in range(board_size):
        player_row = " ".join(player_board[row])
        bot_row = " ".join(bot_board[row]).replace("=", ".")
        print("   %s %s\t%s %s") % \
            (alphabet[letter], player_row,\
             alphabet[letter], bot_row)
        letter += 1


def ship_placement_check(board, x, y, is_horisontal, ship_len):
    no_errors = False
    while no_errors == False:
        # cannot be out of the board
        if x + ship_len > 9 or y + ship_len > 9:
            print("Out of the board")
            no_errors = False; continue
        # cannot cross other ship
        # cannot be closer than 1 sell to other ship
        elif x > 1 and x < 9 and y > 1 and y < 9:
            for diapazon in range(-1,2):
                for ship_sell in range(ship_len):
                    if is_horisontal == 1:
                        if board[x + ship_sell + diapazon][y] == "=": no_errors = False; continue
                    if is_horisontal == 0:
                        if board[x][y + ship_sell + diapazon] == "=": no_errors = False; continue
        else: no_errors = True
    return True

def ships_placement(board,ship):
    ship_len = 4
    no_errors = False
    while no_errors == False:
        x = random.randint(0,9)
        y = random.randint(0,9)
        is_horisontal = random.randint(0,1)
        print ("x=%s y=%s len=%s is_hor=%s") % (x,y,ship_len,is_horisontal)
        no_errors = ship_placement_check(board, x, y, is_horisontal, ship_len)
    for sell in range(ship_len):
        if is_horisontal == 1:
            board[x + sell][y] = "="
        elif is_horisontal == 0:
            board[x][y + sell] = "="
    return board,x,y,ship_len

def ships(board):
    ships = {
        4 : ([0,0,0]),
        3 : ([0,0,0],[0,0,0]),
        2 : ([0,0,0],[0,0,0],[0,0,0]),
        1 : ([1,1,1],[0,0,0],[0,0,0],[0,0,0])
    }
    for ship_type in range(1,5):
        for ship in range(1,5-ship_type):
            print(ships[ship_type][ship])


# FINAL ACT. The Game.
if __name__ == "__main__":
    board_size = 10
    player_board = generate_board(board_size)
    bot_board = generate_board(board_size)
    show_boards(player_board, bot_board, board_size)
    ships(player_board)
