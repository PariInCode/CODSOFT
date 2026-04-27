import random

board = [' '] * 9


def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def player_move():
    position = int(input("Enter position (0-8): "))

    if board[position] == ' ':
        board[position] = 'X'
    else:
        print("Position already taken!")
        player_move()


def check_winner(symbol):
    win_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in win_positions:
        if board[combo[0]] == symbol and board[combo[1]] == symbol and board[combo[2]] == symbol:
            return True

    return False


def minimax(is_maximizing):

    if check_winner('O'):
        return 1
    elif check_winner('X'):
        return -1
    elif ' ' not in board:
        return 0

    if is_maximizing:
        best_score = -100

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(best_score, score)

        return best_score


def ai_move():
    best_score = -100
    best_move = 0

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = 'O'
    print("AI chose position:", best_move)


print("🎮 Welcome to Tic Tac Toe AI")
print("You = X")
print("AI = O")
print()
print("Board positions:")
print(" 0 | 1 | 2")
print("---+---+---")
print(" 3 | 4 | 5")
print("---+---+---")
print(" 6 | 7 | 8")

while ' ' in board:

    print_board()
    player_move()

    if check_winner('X'):
        print_board()
        print("🎉 You Win!")
        break

    if ' ' not in board:
        break

    ai_move()

    if check_winner('O'):
        print_board()
        print("🤖 AI Wins!")
        break

if not check_winner('X') and not check_winner('O'):
    print_board()
    print("🤝 Draw!")