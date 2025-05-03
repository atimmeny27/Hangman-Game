import random
import hangman_art  # This is a separate .py file I made with the ascii art
import words  # This is a separate .py file with a long list of words

words = words.selection

hangman_art = {0: (hangman_art.stage_zero),
               1: (hangman_art.stage_one),
               2: (hangman_art.stage_two),
               3: (hangman_art.stage_three),
               4: (hangman_art.stage_four),
               5: (hangman_art.stage_five),
               6: (hangman_art.stage_six)}


def display_man(wrong_guesses):
    """Displays the hangman art based on the number of wrong guesses"""
    # Make sure to limit wrong_guesses to prevent index out of range
    wrong_guesses = min(wrong_guesses, 6)
    print(hangman_art[wrong_guesses])  # Prints the current stage of hangman art


def display_hint(hint):
    """Displays the current hint with guessed letters and underscores"""
    print(" ".join(hint))  # Joins the list of hint with spaces for easy readability


def display_answer(answer):
    """Displays the final answer when the game is over"""
    print("The word was: " + answer)


def main():
    """Main function for running the hangman game"""
    answer = random.choice(words)  # Randomly selects a word from the word list
    hint = ["_"] * len(answer)  # Initializes the hint with underscores for each letter
    wrong_guesses = 0  # Initializes the wrong guess count
    guessed_letters = set()  # Set to track guessed letters
    is_running = True  # Game status flag

    while is_running:
        display_man(wrong_guesses)  # Displays the current hangman art
        display_hint(hint)  # Displays the current hint (with guessed letters)

        guess = input("Enter a letter: ").lower()  # Takes player input and makes it lowercase

        # Validates the input: only one letter, and must be alphabetical
        if len(guess) != 1 or not guess.isalpha():
            print("One letter please!")
            continue

        # If the letter has already been guessed, skip
        if guess in guessed_letters:
            print(f"{guess} has already been guessed")
            continue

        guessed_letters.add(guess)  # Adds the letter to guessed set

        if guess in answer:
            # Update the hint if the guess is in the answer
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            # Increment wrong guesses if the guess was incorrect
            wrong_guesses += 1

        # Check if the player has guessed the entire word or lost
        if "_" not in hint:
            print("Congratulations! You've guessed the word!")
            display_answer(answer)
            break  # Ends the game if the word is fully guessed

        if wrong_guesses >= 6:
            print("You lost! The word was:")
            display_answer(answer)
            break  # Ends the game if the player has lost


if __name__ == "__main__":
    main()
