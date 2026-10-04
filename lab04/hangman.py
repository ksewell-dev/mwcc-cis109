import random

# Step 1: Create a list of words for the game.
wordlist = [
    "hangman",
    "llama",
    "python"
]

# Step 2: Randomly select a word from the list.
random_number = random.randint(0, len(wordlist) - 1)
word = wordlist[random_number]

# Step 3: Create a list to store incorrect guesses.
bad_guesses = []

# Step 4: Create the game board using underscores.
board = []

for letter in word:
    board.append("_")

# Step 5: Repeat the game until the player wins or runs out of guesses.
while True:
    print()
    print("Welcome to HANGMAN!")
    print()
    print(board)
    print()

    # Step 6: Display the hangman drawing based on the number of incorrect guesses.
    match len(bad_guesses):
        case 1:
            print('''
+---+
|
|
|
|
=======
'''.strip())
        case 2:
            print('''
+---+
|   |
|
|
|
=======
'''.strip())
        case 3:
            print('''
+---+
|   |
|   0
|
|
=======
'''.strip())
        case 4:
            print('''
+---+
|   |
|   0
|   |
|
=======
'''.strip())
        case 5:
            print('''
+---+
|   |
|   0
|  /|\\
|
=======
'''.strip())
        case 6:
            print('''
+---+
|   |
|   0
|  /|\\
|  / \\
=======
'''.strip())

    # Step 7: Display the incorrect guesses.
    print()
    print("Bad Guesses:", bad_guesses)
    print()

    # Step 8: End the game after six incorrect guesses.
    if len(bad_guesses) == 6:
        break

    # Step 9: Ask the player for a letter and convert it to lowercase.
    guess = input("Guess a letter: ").lower()

    # Step 10: Check that the player entered one letter.
    if len(guess) != 1 or not guess.isalpha():
        print()
        print("⚠️ Please enter one letter.")
        input("Press [enter] to continue.")
        continue

    # Step 11: Check that the letter has not already been guessed.
    if guess in bad_guesses or guess in board:
        print()
        print("⚠️ You already guessed that letter!")
        input("Press [enter] to continue.")
        continue

    # Step 12: Check the guess against each letter in the word.
    is_found = False

    for i, letter in enumerate(word, start=0):
        if letter == guess:
            board[i] = word[i]
            is_found = True

    # Step 13: Give feedback and check whether the player has won.
    if is_found:
        print()
        print(f"✅ '{guess}' is in the word!")
        input("Press [enter] to continue.")

        if "_" not in board:
            break
    else:
        # Step 14: Add an incorrect guess to the bad guesses list.
        bad_guesses.append(guess)
        print()
        print(f"❌ '{guess}' is not in the word.")
        input("Press [enter] to continue.")

# Step 15: Display the final result.
if "_" not in board:
    print()
    print(f"🎉 YOU WON! The word was '{word}'")
else:
    print()
    print(f"💀 YOU LOST! The word was '{word}'")

# Step 16: Thank the player for playing.
print()
print("Thank you for playing!")
