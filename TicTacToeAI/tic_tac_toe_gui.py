import tkinter as tk
from tkinter import messagebox

board = [' '] * 9
buttons = []

root = tk.Tk()
root.title("Tic Tac Toe AI")
root.geometry("360x450")
root.config(bg="#1e1e1e")


def check_winner(symbol):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for combo in wins:
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
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = 100

        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)

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
    buttons[best_move].config(text="O", state="disabled")

    if check_winner('O'):
        messagebox.showinfo("Game Over", "AI Wins 🤖")
        disable_all()
    elif ' ' not in board:
        messagebox.showinfo("Game Over", "Draw!")


def click(index):
    if board[index] == ' ':
        board[index] = 'X'
        buttons[index].config(text="X", state="disabled")

        if check_winner('X'):
            messagebox.showinfo("Game Over", "You Win 🎉")
            disable_all()
            return

        if ' ' not in board:
            messagebox.showinfo("Game Over", "Draw!")
            return

        ai_move()


def disable_all():
    for btn in buttons:
        btn.config(state="disabled")


def restart():
    global board
    board = [' '] * 9

    for btn in buttons:
        btn.config(text="", state="normal")


title = tk.Label(root, text="Tic Tac Toe AI", font=("Arial", 20, "bold"),
                 bg="#1e1e1e", fg="white")
title.pack(pady=10)

frame = tk.Frame(root, bg="#1e1e1e")
frame.pack()

for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 24, "bold"),
                    width=5, height=2,
                    command=lambda i=i: click(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

restart_btn = tk.Button(root, text="Restart Game", font=("Arial", 14),
                        command=restart, bg="green", fg="white")
restart_btn.pack(pady=20)

root.mainloop()