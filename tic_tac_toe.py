print("WELCOME TO TIC TAC TOE GAME")
print("___________________________")
possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows = 3
cols = 3


def game_board():
    for x in range(rows):
        print("\n|---|---|---|")
        print(end="|")
        for y in range(cols):
            print("", board[x][y], "", end="|")
    print("\n|---|---|---|")


game_board()


def modify_array(num, turn):
    num -= 1
    if num == 0:
        board[0][0] = turn
    elif num == 1:
        board[0][1] = turn
    elif num == 2:
        board[0][2] = turn
    elif num == 3:
        board[1][0] = turn
    elif num == 4:
        board[1][1] = turn
    elif num == 5:
        board[1][2] = turn
    elif num == 6:
        board[2][0] = turn
    elif num == 7:
        board[2][1] = turn
    elif num == 8:
        board[2][2] = turn


for i in range(9):
    if board[0][0] == board[1][1] == board[2][2] == 'x' or board[0][2] == board[1][1] == board[2][0] == 'x' or board[0][
        2] == board[1][2] == board[2][2] == 'x' or board[2][0] == board[2][1] == board[2][2] == 'x' or board[0][1] == \
            board[1][1] == board[2][1] == 'x' or board[0][0] == board[1][0] == board[2][0] == 'x' or board[1][0] == \
            board[1][1] == board[1][2] == 'x' or board[0][0] == board[0][1] == board[0][2] == 'x':
        print("\nX is the winner")
        break
    elif board[0][0] == board[1][1] == board[2][2] == 'o' or board[0][2] == board[1][1] == board[2][0] == 'o' or \
            board[0][
                2] == board[1][2] == board[2][2] == 'o' or board[2][0] == board[2][1] == board[2][2] == 'o' or board[0][
        1] == \
            board[1][1] == board[2][1] == 'o' or board[0][0] == board[1][0] == board[2][0] == 'o' or board[1][0] == \
            board[1][1] == board[1][2] == 'o' or board[0][0] == board[0][1] == board[0][2] == 'o':
        print("\nO is the winner")
        break
    if (i % 2) == 0:
        print("Turn of x")
        a = int(input("Enter the value:"))
        b = "x"
    else:

        print("Turn of o")
        a = int(input("Enter the value:"))
        b = "o"
    modify_array(a, b)
    game_board()


