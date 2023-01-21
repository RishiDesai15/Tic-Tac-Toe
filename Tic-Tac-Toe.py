
board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currPlayer = "X"
winner = None
gamerunning = True

# Creating Game Board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(" " * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(" " * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

# Player Input
def playerInput(board):
    while True:
        if currPlayer == "X":
            inp = int(input(f"Enter a number 1-9 \033[1;44m X \033[0;0m : "))
        else:
            inp = int(input(f"Enter a number 1-9 \033[1;41m 0 \033[0;0m : "))
        if (inp >= 1 and inp <= 9) and (board[inp-1] == "-"):
            board[inp-1] = currPlayer
            break
        print("Spot Already Taken!")

# Checking Win or Tie
def Row(board):
    global winner
    if (board[0] == board[1] == board[2]) and (board[1] != "-"):
        winner = board[0]
        return True
    elif (board[3] == board[4] == board[5]) and (board[4] != "-"):
        winner = board[3]
        return True
    elif (board[6] == board[7] == board[8]) and (board[7] != "-"):
        winner = board[6]
        return True

def Column(board):
    global winner
    if (board[0] == board[3] == board[6]) and (board[3] != "-"):
        winner = board[0]
        return True
    elif (board[1] == board[4] == board[7]) and (board[4] != "-"):
        winner = board[1]
        return True
    elif (board[2] == board[5] == board[8]) and (board[5] != "-"):
        winner = board[2]
        return True

def Diagonal(board):
    global winner
    if (board[0] == board[4] == board[8]) and (board[0] != "-"):
        winner = board[0]
        return True
    elif (board[2] == board[4] == board[6]) and (board[2] != "-"):
        winner = board[2]
        return True

def Tie(board):
    global gamerunning
    if "-" not in board:
        printBoard(board)
        print("Its a Tie!")
        gamerunning = False

def winnerCheck():
    if Diagonal(board) or Row(board) or Column(board):
        print(f"The winner is {winner}")

# Switch Player
def switchPlayer():
    global currPlayer
    if currPlayer == "X":
        currPlayer = "O"
    else:
        currPlayer = "X"

# Checking Win or Tie
while gamerunning:
    printBoard(board)
    if winner != None:
        break
    playerInput(board)
    winnerCheck()
    Tie(board)
    switchPlayer()