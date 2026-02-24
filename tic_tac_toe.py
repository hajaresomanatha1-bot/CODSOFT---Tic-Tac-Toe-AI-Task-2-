# Tic Tac Toe AI
# CODSOFT AI Internship - Task 2

import random

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_draw():
    return " " not in board

def player_move():
    move = int(input("Enter position (1-9): ")) - 1
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Position already taken!")
        player_move()

def ai_move():
    print("AI is making a move...")
    empty_positions = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty_positions)
    board[move] = "O"

def game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        player_move()
        print_board()

        if check_winner("X"):
            print("You win! 🎉")
            break
        if is_draw():
            print("It's a draw!")
            break

        ai_move()
        print_board()

        if check_winner("O"):
            print("AI wins! 🤖")
            break
        if is_draw():
            print("It's a draw!")
            break

game()
