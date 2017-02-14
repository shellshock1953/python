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
    print("     %s\t  %s") % (str(numbers), str(numbers))
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


def manual_ship_placement(board,ship_len):
    print ("Select leng: 4")
    leng = 4
    print ("Use H J K L to move")
    print ("Use V to switch to vertical")
    print ("User E to select")
    x, y = selector(player_board, bot_board)
    print x,y


    
def ships(board):
    ships = {
        4 : ([0,0,0],),
        3 : ([0,0,0],[0,0,0]),
        2 : ([0,0,0],[0,0,0],[0,0,0]),
        1 : ([1,1,1],[0,0,0],[0,0,0],[0,0,0])
    }
    for ship_type in range(1,5):
        for ship in range(0,5-ship_type):
            board, ships[ship_type][ship][0], \
            ships[ship_type][ship][1], \
            ships[ship_type][ship][2] = ship_placement(board,ship_type)
    print(ships)

def selector(board_orig,bot_board):
    import copy
    x = 4
    y = 4
    board = copy.deepcopy(board_orig)
    board[x-1][y-1] = "+"
    board[x-1][y+1] = "+"
    board[x+1][y-1] = "+"
    board[x+1][y+1] = "+"
    while True:
        board = copy.deepcopy(board_orig)
        arrow = raw_input()
        if arrow == "h": y = y - 1
        elif arrow == "j": x = x + 1
        elif arrow == "k": x = x - 1
        elif arrow == "l": y = y + 1
        elif arrow == "e":
            print coordinated_to_alpha(x,y)
            return x,y
        board[x-1][y-1] = "+"
        board[x-1][y+1] = "+"
        board[x+1][y-1] = "+"
        board[x+1][y+1] = "+"
        show_boards(board,bot_board, 10)


def coordinated_to_alpha(x,y):
    alphabet = string.uppercase
    alpha_x = alphabet[x]
    alpha_y = y + 1
    alpha_coordinates = str(alpha_x) + str(alpha_y)
    return alpha_coordinates


def coordinated_to_num(alpha_x, alpha_y):
    alphabet = string.uppercase
    x = str(alphabet).index(alpha_x)
    y = int(alpha_y) - 1
    return x,y

# FINAL ACT. The Game.
if __name__ == "__main__":
    board_size = 10
    player_board = generate_board(board_size)
    bot_board = generate_board(board_size)
    show_boards(player_board, bot_board, board_size)
    manual_ship_placement(player_board,4)
    
