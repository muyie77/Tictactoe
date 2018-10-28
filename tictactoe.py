from random import randint
import os
# Global Variables
cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win_combo = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
win = 0
lose = 0
no_win = 0

# Drawing the board
def board():
    os.system('cls')
    print(f"Win: {win}\t\tLose: {lose}\t\tNo Winner: {no_win}")
    print("           |           |           ")
    print("           |           |           ")
    print(f"     {cells[0]}     |     {cells[1]}     |     {cells[2]}      ")
    print("           |           |           ")
    print("           |           |           ")
    print("-----------+-----------+-----------")
    print("           |           |           ")
    print("           |           |           ")
    print(f"     {cells[3]}     |     {cells[4]}     |     {cells[5]}      ")
    print("           |           |           ")
    print("           |           |           ")
    print("-----------+-----------+-----------")
    print("           |           |           ")
    print("           |           |           ")
    print(f"     {cells[6]}     |     {cells[7]}     |     {cells[8]}      ")
    print("           |           |           ")
    print("           |           |           ")

# Player
def player():
    print("Select number of box:", end =" ")

    while True:
        choice = int(input())
        choice -= 1

        if cells[choice] == 'X' or cells[choice] == 'O':
            print(f"Box {choice + 1} is not available. Choose another box.")
        else:
            cells[choice] = 'X'
            break

# Computer
def computer():
    while True:
        choice = randint(1, 9)
        choice -= 1

        if cells[choice] == 'X' or cells[choice] == 'O':
            """ """
        else:
            cells[choice] = 'O'
            break

#Check for winner
def check_win():
    global win, lose, no_win
    for n in win_combo:
        a, b, c = n
        if cells[a] == cells[b] == cells[c] == 'X':
            win += 1
            board()
            print("Congratulations. You win!")
            return 1
        elif cells[a] == cells[b] == cells[c] == 'O':
            board()
            print("Sorry. You lose.")
            lose += 1
            return 1
# The main function. Where the game starts.
def main():
    while check_win() != 1:
        board()
        player()
        computer()
        check_win()

# Ask the player to play again or not after the game.
def play_again():
    print("Do you want to play again? y/n")
    while True:
        ch = input("> ")
        if ch == 'y' or ch == 'Y':
            main()
            break
        elif ch == 'n' or ch == 'N':
            exit(0)
        else:
            print("Invalid choice!\n")

main()
play_again()



#PROBLEMS!!!!!!!
#1. If all the boxes are not available, the game stucks.
#2. No output for "No winner"
#3. If you choose to play again, boxes doesn't resets
#4. After the game, scores increments by 2 instead of 1 (win, lose, draw)
