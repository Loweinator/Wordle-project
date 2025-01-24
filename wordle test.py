import random

class colors:
    GREEN = '\033[92m'   # Green for correct letter in the correct position
    YELLOW = '\033[93m'  # Yellow for correct letter but in the wrong position
    RESET = '\033[0m'    # Reset to default color after each colored letter

def load_word_list():
    # A small sample of 5-letter words; you can replace this with a larger list or load from a file.
    return ['apple', 'banjo', 'candy', 'dance', 'flame', 'grape', 'house', 'ivory', 'jolly', 'lunar', 'steak', 'cloud']

def get_guess():
    guess = input("Enter your 5-letter guess: ").strip().lower()
    while len(guess) != 5 or not guess.isalpha():
        print("Invalid input! Please enter a 5-letter word.")
        guess = input("Enter your 5-letter guess: ").strip().lower()
    return guess

def give_feedback(guess, target_word):
    feedback = []
    # To keep track of which letters have been matched for yellow feedback
    target_word_copy = list(target_word)

    for i in range(len(guess)):
        if guess[i] == target_word[i]:
            # Correct letter in the correct position: GREEN
            feedback.append(f"{colors.GREEN}{guess[i].upper()}{colors.RESET}")
            target_word_copy[i] = None  # Mark this position as matched
        elif guess[i] in target_word_copy:
            # Correct letter but in the wrong position: YELLOW
            feedback.append(f"{colors.YELLOW}{guess[i].upper()}{colors.RESET}")
            target_word_copy[target_word_copy.index(guess[i])] = None  # Mark this letter as matched
        else:
            # Incorrect letter: No color
            feedback.append(guess[i])
    
    return ''.join(feedback)

def play_wordle():
    word_list = load_word_list()
    target_word = random.choice(word_list)
    attempts = 6

    print("Welcome to Wordle!")
    print("You have 6 attempts to guess the 5-letter word.")
    
    while attempts > 0:
        print(f"\nYou have {attempts} attempts left.")
        guess = get_guess()

        if guess == target_word:
            print("Congratulations! You've guessed the word correctly!")
            break
        
        feedback = give_feedback(guess, target_word)
        print("Feedback: ", feedback)
        attempts -= 1

    if attempts == 0:
        print(f"Sorry, you've run out of attempts! The word was: {target_word}")

# Run the game
if __name__ == "__main__":
    play_wordle()
