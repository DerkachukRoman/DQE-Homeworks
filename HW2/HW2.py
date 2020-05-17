from sys import exit
from random import choice


def print_board():
    for i in range(3):
        print(board[0+i*3], "|", board[1+i*3], "|", board[2+i*3])
        if i != 2:
            print("--|---|---")
    print("\n\n")


def player_input():
    org_position = input \
        ("Player, it's your turn. Please chose position [1-9]: ")
    if int(org_position) not in range(1,10):
        print("Enter a valid position!")
        player_input()
    else:
        position = int(org_position) - 1
        if board[position] == "X" or board[position] == "O":
            print("Position occupied!")
            player_input()
        else:
            board[position] = player_symbol
    free.remove(position+1)
    return (position+1)


def computer_move():
    move = -1
    ai_win = False
    #Check if computer can win
    for i in range(1,10):
        if board[i-1] == i and can_win(computer_symbol, i, True):
            move = i
            print("Computer wins!")
            ai_win = True
            break
    
    if move == -1:
        #Block if player can win
        for i in range(1,10):
            if board[i-1] == i and can_win(player_symbol, i, True):
                move = i
                break
    
    if move == -1:
        #Random position
        for mv in board:
            if move == -1 and str(mv) not in "OX":
                move = choice(free)
                break
    board[move-1] = computer_symbol
    free.remove(move)
    return ai_win


def can_win(symbol, move, ret=False):
    win = True
    board[move-1] = symbol
    for tup in winning_positions:
        win=True
        for ix in tup:
            if board[ix] != symbol:
                win=False
                break
        if win == True:
            break
    if ret:
        board[move-1] = move
    return win



board = [i for i in range(1,10)]
free =  [i for i in range(1,10)]

winning_positions = ((0,1,2),(3,4,5),(6,7,8),
                 (0,3,6),(1,4,7),(2,5,8),
                 (0,4,8),(2,4,6))

player_symbol, computer_symbol = "", ""
    
while True:
    smb = input("Please choose your symbol (X or O):")

    if smb in "xX":
        player_symbol += 'X'
        computer_symbol += 'O'
        break
    elif smb in "oO":
        player_symbol += 'O'
        computer_symbol += 'X'
        break
    else:
        print("Your symbol is invalid!")

count = 0

while count <= 8:

    if player_symbol == 'X':
        print_board()
        if can_win(player_symbol, player_input()):
            print("Congratulation, you are winner.")
            print_board()
            exit(0)
        if count != 8:
            if computer_move():
                print_board()
                exit(0)
    else:
        if computer_move():
            print_board()
            exit(0)
        if count == 8:
            break
        print_board()
        if can_win(player_symbol, player_input()):
            print("Congratulation, you are winner.")
            print_board()
            exit(0)

    count += 2

print_board()
print("It's a Tie.")

