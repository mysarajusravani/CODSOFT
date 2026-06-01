import math

cell_positions = [" " for _ in range(9)]

def show_board():
    print()
    for i in range(3):
        print(" | ".join(cell_positions[i * 3:(i + 1) * 3]))
        if i < 2:
            print("-" * 9)
    print()

def check_victory(player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    for pattern in win_patterns:
        if all(cell_positions[pos] == player for pos in pattern):
            return True
    return False

def is_tie():
    return " " not in cell_positions

def evaluate_move(is_maximizing):
    if  check_victory("O"):
        return 1
    if  check_victory("X"):
        return -1
    if  is_tie():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if cell_positions[i] == " ":
                cell_positions[i] = "O"
                score = evaluate_move(False)
                cell_positions[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if cell_positions[i] == " ":
                cell_positions[i] = "X"
                score = evaluate_move(True)
                cell_positions[i] = " "
                best_score = min(score, best_score)

        return best_score

def bot_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if cell_positions[i] == " ":
            cell_positions[i] = "O"
            score = evaluate_move(False)
            cell_positions[i] = " "

            if score > best_score:
                best_score = score
                move = i

    cell_positions[move] = "O"

def user_move():
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1

            if 0 <= pos < 9 and cell_positions[pos] == " ":
                cell_positions[pos] = "X"
                break
            else:
                print("Invalid move!")

        except ValueError:
            print("Enter a valid number!")

print("=== TIC TAC TOE AI ===")
print("You are X")
print("Positions:")
print("1 | 2 | 3")
print("---------")
print("4 | 5 | 6")
print("---------")
print("7 | 8 | 9")

while True:
    show_board()

    user_move()

    if check_victory("X"):
        show_board()
        print("You Win")
        break

    if is_tie():
        show_board()
        print("It's a tie")
        break

    bot_move()

    if check_victory("O"):
        show_board()
        print("AI Wins")
        break

    if is_tie():
        show_board()
        print("It's a tie")
        break
