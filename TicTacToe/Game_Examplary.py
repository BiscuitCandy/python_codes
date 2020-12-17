board = [
    ["0", "#",  "#"],
    ["0", "#",  "#"],
    ["0", "#",  "#"]
]

def columnpass(board) :

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] in ["X", "0"]:
            return board[0][i]
    return False

print(columnpass(board))
