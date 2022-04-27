# @see https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
def graphics(chances):
    pics = [
        "\n                    +---+\n\t\t        |\n\t\t        +\n\t\t        |\n\t\t        |\n\t\t        |\n==========================",
        "\n                    +---+\n\t\t    |   |\n\t\t        |\n\t\t        |\n\t\t        |\n\t\t        |\n==========================",
        "\n                    +---+\n\t\t    |   |\n\t\t    O   |\n\t\t        |\n\t\t        |\n\t\t        |\n==========================",
        "\n                    +---+\n\t\t    |   |\n\t\t    O   |\n\t\t    |   |\n\t\t        |\n\t\t        |\n==========================",
        "\n                    +---+\n\t\t    |   |\n\t\t    O   |\n\t\t   /|   |\n\t\t        |\n\t\t        |\n==========================",
        "\n                    +---+\n\t\t    |   |\n\t\t    O   |\n\t\t   /|\  |\n\t\t        |\n\t\t        |\n==========================",
        "\n                    +---+\n\t\t    |   |\n\t\t    O   |\n\t\t   /|\  |\n\t\t   /    |\n\t\t        |\n==========================",
        "\n                    +---+\n\t\t    |   |\n\t\t    O   |\n\t\t   /|\  |\n\t\t   / \  |\n\t\t        |\n=========================="
    ]
    return pics

def is_valid_guess(guess):
    if len(guess) == 1 & guess.isalpha():
        return True
    else:
        return False

# @see https://stackoverflow.com/a/15195942/4896064
def mask_word(state, word, guess):
    state = list(state)
    for i in range(len(word)):
        if word[i] == guess:
            state[i] = guess
    return "".join(state)


def play_game(file):
    with open(file, "r") as f:
        # TODO: get random word from file
        word = f.read().upper()
        # print(f"DEBUG :: word={word}")

        state = "—" * len(word)

    # chances
    chances = 8

    # list of guesses
    guesses = []

    # graphics
    pics = graphics(chances)

    while(True):

        print(pics[len(guesses)])
        
        mask = " ".join(state)
        print(f"{mask}")
        print(f"({len(word)} letters)\n")

        # get guess
        guess = input("Please guess a letter: ").upper()
        # print(f"DEBUG :: guess={guess}")

        # Guess is invalid
        if is_valid_guess(guess) == False:
            print(f"Whooops! '{guess}' is not a valid guess.")
        # Guess is valid
        else:
            # Check if already guessed
            if guess in guesses:
                print(f"You already guessed {guess}.")
                # print(f"DEBUG :: guesses={guesses}")
            else:

                # Correct guess
                if guess in word:
                    state = mask_word(state, word, guess)
                
                    if mask_word(state, word, guess) == word:
                        print(f"WIN!! You guessed correctly.")
                        print(state)
                        break
                # Incorrect guess
                else:
                    guesses.append(guess)
                    print(f"FAIL!, {guess} is knot a winner.")

                    # print(f"DEBUG :: guesses={guesses}")

                    if len(guesses) == chances:
                        print(f"Oh no! You're out of gueeses.")
                        print(f"The word is {word}.")
                        break
                    else:
                        # Remind the user of how many guesses they have left after each round.
                        print(f"{chances - len(guesses)} guesses remaining...")

# if __name__ == "__main__":
play_game("test-word.txt")
