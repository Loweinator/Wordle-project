import random

class colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    END = '\033[0m'

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
    for i in range(len(guess)):
        if guess[i] == target_word[i]:
            feedback.append(f"[{guess[i].upper()}]")  # Correct letter in the correct position
        elif guess[i] in target_word:
            feedback.append(f"({guess[i]})")  # Correct letter but in the wrong position
        else:
            feedback.append(guess[i])  # Incorrect letter
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
