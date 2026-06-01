import random

words = ["python", "programming", "computer", "hangman", "developer"]

word = random.choice(words)

guessed_letters = []

attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    display_word = ""

    # Build the displayed word
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is fully guessed
    if "_" not in display_word:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        attempts -= 1
        print(f"Wrong guess! Attempts left: {attempts}")
    else:
        print("Correct!")

else:
    print("\nGame Over! The word was:", word)