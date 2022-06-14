def main():
    player = next_player("")
    grid = drawGrid()
    while not (winner(grid) or is_a_draw(grid)):
        drawBoard(grid)
        make_move(player, grid)
        player = next_player(player)
    drawBoard(grid)
    print("Good game. Thanks for playing!") 
def drawGrid():
    tictac = []
    for x in range(9):
        tictac.append(x+1)
    #print(tictac)
    return tictac
def drawBoard(tictac):
    print()
    print(f"{tictac[0]} | {tictac[1]} | {tictac[2]}")
    print(f"-+-+-")
    print(f"{tictac[3]} | {tictac[4]} | {tictac[5]}")
    print(f"-+-+-")
    print(f"{tictac[6]} | {tictac[7]} | {tictac[8]}")
    print()

def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

def winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()
