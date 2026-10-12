# Create a 3x3 matrix with dashes.
matrix = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

# Create a list of players.
players = ["X", "O"]

# Set the number of turns and winner.
turns = 0
winner = None

# Continue until there are 9 turns or a winner.
while turns < 9 and winner is None:
    player = players[turns % 2]

    print()
    print("TIC-TAC-TOE")

    # Display the game board.
    for row in matrix:
        for col, space in enumerate(row):
            if col > 0:
                print("|", end=" ")
            print(space, end=" ")
        print()

    # Display the current player and ask for a row and column.
    print()
    print(f"{player}'s Turn")

    row = input("Enter row (1-3): ")
    col = input("Enter column (1-3): ")

    # Check for invalid input.
    if not row.isdigit() or not col.isdigit():
        print("Invalid input. Please enter numbers from 1 to 3.")
        continue

    row = int(row)
    col = int(col)

    if row < 1 or row > 3 or col < 1 or col > 3:
        print("Invalid row or column. Please enter 1, 2, or 3.")
        continue

    # Check if the space has already been claimed.
    if matrix[row - 1][col - 1] != "-":
        print(f"Someone has already claimed {row}:{col}!")
        input("Hit [enter] to continue.")
        continue

    # Place the player's marker on the board.
    matrix[row - 1][col - 1] = player

    # Check for a horizontal or vertical win.
    for i in range(3):
        if matrix[i][0] == matrix[i][1] == matrix[i][2] == player:
            winner = player

        if matrix[0][i] == matrix[1][i] == matrix[2][i] == player:
            winner = player

    # Check for a diagonal win.
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == player:
        winner = player

    if matrix[0][2] == matrix[1][1] == matrix[2][0] == player:
        winner = player

    # Increment the number of turns.
    turns += 1

# Display the final game board.
print()
print("TIC-TAC-TOE")

for row in matrix:
    for col, space in enumerate(row):
        if col > 0:
            print("|", end=" ")
        print(space, end=" ")
    print()

# Display the winner or a draw.
if winner is not None:
    print()
    print(f"{winner} won!")
else:
    print()
    print("It's a draw!")

print("Game Over!")
print("Thanks for playing!")
