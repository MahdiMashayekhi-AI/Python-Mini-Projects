board = [' ' for x in range(10)]

def print_board(board):
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + " ")
    print("-----------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("-----------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + " ")

def insert_letter(letter, pos):
    board[pos] = letter

def space_is_free(pos):
    return board[pos] == ' '

def is_board_full(board):
    return board.count(' ') == 1

def is_winner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
            (b[4] == l and b[5] == l and b[6] == l) or
            (b[7] == l and b[8] == l and b[9] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[3] == l and b[6] == l and b[9] == l) or
            (b[1] == l and b[5] == l and b[9] == l) or
            (b[3] == l and b[5] == l and b[7] == l))

def player_move():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move in range(1, 10):
                if space_is_free(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print("Sorry, this space is already occupied.")
            else:
                print("Please type a number within the range.")
        except:
            print("Please type a number.")

def computer_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for letter in ['O','X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = letter
            if is_winner(board_copy, letter):
                move = i
                return move

    corner_moves = []
    for i in possible_moves:
        if i in [1,3,7,9]:
            corner_moves.append(i)
    if len(corner_moves) > 0:
        move = select_random(corner_moves)
        return move

    center_moves = []
    if 5 in possible_moves:
        center_moves.append(5)
    if len(center_moves) > 0:
        move = select_random(center_moves)
        return move

    side_moves = []
    for i in possible_moves:
        if i in [2,4,6,8]:
            side_moves.append(i)
    if len(side_moves) > 0:
        move = select_random(side_moves)

    return move

def select_random(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while not(is_board_full(board)):
        if not(is_winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print("Sorry, O's won this time!")
            break

        if not(is_winner(board, 'X')):
            move = computer_move()
            if move == 0:
                print("Tie game!")
            else:
                insert_letter('O', move)
                print("Computer placed an 'O' in position", move, ":")
                print_board(board)
        else:
            print("X's won this time! Good job!")
            break

    if is_board_full(board):
        print("Tie game!")

main()
