import tkinter as tk
from tkinter import messagebox
import random
# Constants
PLAYER_X = "X"
PLAYER_O = "O"
WIN_COMBINATIONS = [
    # Rows
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    # Columns
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    # Diagonals
    [0, 4, 8],
    [2, 4, 6]
]

# Initialize the board
gameboard = [" "] * 9

# Initialize the GUI
root = tk.Tk()
root.title("Tic-Tac-Toe game")

# Create the buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", width=10, height=5,command=lambda index=i: button_click(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Function to handle button clicks
def button_click(index):
    if gameboard[index] == " ":
        # Update the board and GUI
        gameboard[index] = PLAYER_X
        buttons[index].config(text=PLAYER_X)
        buttons[index].config(state=tk.DISABLED)
        # Check for a win or tie
        if check_win(PLAYER_X):
            stop_game("Player X wins!")
        elif check_full_board():
            stop_game("It's a tie!")
        else:
            # Let the AI make a  random move
            ai_random_move()
            # Let the AI make a  row wise move
            #ai_row_move()
# In this AI move will be in row wise move
def ai_row_move():
    # Find an empty spot and make a move
    for i in range(9):
        if gameboard[i] == " ":
            gameboard[i] = PLAYER_O
            buttons[i].config(text=PLAYER_O)
            buttons[i].config(state=tk.DISABLED)
            if check_win(PLAYER_O):
                stop_game("Player O wins!")
            break

# In this AI move will be random
def ai_random_move():
    # Check for available moves
    available_moves = []
    for i in range(9):
        if gameboard[i] == ' ':
            available_moves.append(i)
    if len(available_moves) > 0:
        # Make a random move
        i = random.choice (available_moves)
        buttons[i].config(text="O")
        gameboard[i] = 'O'

        buttons[i].config(state=tk.DISABLED)
        if check_win(PLAYER_O):
            stop_game("Player O wins!")

# Function to check for a win
def check_win(player):
    for combination in WIN_COMBINATIONS:
        if all(gameboard[i] == player for i in combination):
            return True
    return False

# Function to check if the board is full
def check_full_board():
    return all(cell != " " for cell in gameboard)

# Function to end the game
def stop_game(message):
    messagebox.showinfo("Result", message)
    root.quit()

# Bind button clicks to the button_click function
for i in range(9):
    buttons[i].config(command=lambda index=i: button_click(index))  # config is to configure the properties after defining

# Start the GUI event loop
#To make the board appear until manual close
root.mainloop()