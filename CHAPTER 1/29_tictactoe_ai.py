board = [' '] * 9

def win(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[i]==b[j]==b[k]==p for i,j,k in wins)

def best_move():
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if win(board, 'O'):
                return i
            board[i] = ' '
    return next(i for i in range(9) if board[i]==' ')

board[0] = 'X'
move = best_move()
board[move] = 'O'
print(board)