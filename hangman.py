

import random

words = ["apple", "tiger", "python", "school", "laptop"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("WELCOME TO HANGMAN GAME!")

while wrong_guesses < max_attempts:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses)

    if "_" not in display_word:
        print("Congratulations! You won!")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter.")
    elif guess in guessed_letters:
        print("You already guessed that letter!")
    else:
        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

if wrong_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", word)
