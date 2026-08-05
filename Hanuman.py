import random
def hangman():
    words = ["apple", "tiger", "chair", "bread", "cloud"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    print("=== Hangman Game ===")
    while attempts > 0:
        display = ""
        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print("\nWord:", display)
        if "_" not in display:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter.")

        elif guess in word:
            guessed_letters.append(guess)
            print("Correct!")

        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Wrong! Attempts left:", attempts)

    if attempts == 0:
        print("Game Over! The word was:", word)


if __name__ == "__main__":
    hangman()
