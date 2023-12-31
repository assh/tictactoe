from globals import ROWS, COLS, board

def game_condition():
    # Check rows
    for row in range(ROWS):
        if board[row][0] != -1 and board[row][0] == board[row][1] == board[row][2]:
            return board[row][0]
    
    # Check columns
    for col in range(COLS):
        if board[0][col] != -1 and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    
    # Check main diagonal
    if board[0][0] != -1 and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    
    # Check secondary diagonal
    if board[0][2] != -1 and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    # Check for tie
    count = sum(row.count(-1) for row in board)
    if count == 0:
        return -2
    
    return -1