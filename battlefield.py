"""
    make shots like A1, C4
    make up to three diferent types to sheeps - 1, 2, 3 sells
    random it horizontally or vertically
    dont allow be closer then one sell between sheeps
    make user to set ships
    make bot player
"""

def board_generator(size):
    board = []
    for sell in range(size):
        board.append(["O"] * size)
    return board

def board_show(board):
    board_size = len(board[0])
    print "  1 2 3 4 5"
    abc = "abcde"
    i = 0
    for row in range(board_size):
        print abc[i]," ".join(board[row])
        i += 1

def get_coordinates():
    while True:
        alph_coordinate = raw_input("Enter coordinates:")
        x_alph = alph_coordinate[0]
        y_alph = alph_coordinate[1]
        if x_alph in "abcde" and str(y_alph) in str(range(1,6)):
            return alph_coordinate
        else:
            print "Wrong coordinates!"

def coordinate_convertor(alph_coordinate):
    x_alph = alph_coordinate[0]
    y_alph = alph_coordinate[1]
    coordinate_dict = {
        "a":1,
        "b":2,
        "c":3,
        "d":4,
        "e":5.
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
def place_ship_error_check(x, y, ship_len, orientation):

    if int(x) + int(ship_len) > 5 or \
       int(y) + int(ship_len) > 5 :
        print "out of the board"
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
            has_errors = place_ship_error_check(x, y, ship_len, orientation)
        place_ship(x, y, ship_len, orientation, board)
        board_show(board)
        i += 1
        print ""


if __name__ == "__main__":
    board = board_generator(5)
    board_show(board)
    manual_place_ship()
    while True:
        alph_coordinate = get_coordinates()
        shoots(alph_coordinate,board)
        board_show(board)

