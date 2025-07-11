board = [' '] * 9

def print_board():
    for i in range(0, 9, 3):
        print(board[i:i+3])

def make_move(pos, player):
    if board[pos] == ' ':
        board[pos] = player

make_move(0, 'X')
make_move(1, 'O')
make_move(4, 'X')
print_board()