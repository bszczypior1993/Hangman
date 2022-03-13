import random
import time
from xml.dom import ValidationErr

# picks a password out of the list:
def pick_password():
    wordlist = ['cebula', 'doggie', 'badger', 'catchfish', 'stopbarking', 'eatseed']
    word = random.choice(wordlist)
    return word.upper()

password = pick_password()

# guessing game:
def play_hangman(password):

    dashed_password = "_" * len(password)
    letter_guess = []
    phrase_guess = []
    guessed = False
    attempts = 6

  
    
    time.sleep(1)
    print(f"Password: {dashed_password}")
    time.sleep(1)

    while not guessed and attempts > 0:
        print(f"You have {attempts} attempts left. What's your guess? ")
        guess = input().upper()
        time.sleep(1)
        if len(guess) == 1 and guess.isalpha():
            if guess in letter_guess:
                print(f"You already tried {guess}. Try another letter.")
            elif guess not in password:
                print(f"Letter {guess} not in the password! :( Try again.")
                attempts -= 1
                letter_guess.append(guess)
            else:
                print(f"Good job! Letter {guess} is in the password!")
                letter_guess.append(guess)
                dashed_password_as_list = list(dashed_password)
                indices = [i for i, letter in enumerate(password) if letter == guess]
                for index in indices:
                    dashed_password_as_list[index] = guess
                dashed_password = "".join(dashed_password_as_list)
                print(f"Password: {dashed_password}")
                time.sleep(1)
                if "_" not in dashed_password:
                    guessed = True
        elif len(guess) > 1 and guess.isalpha():
            if guess in phrase_guess:
                print(f"You already tried {guess}. Try another phrase.")
            elif guess != password:
                print(f"{guess} is not the correct password! :( Try again.")
                attempts -= 1
                phrase_guess.append(guess)
            else:
                guessed = True
                dashed_password = password
        else:
            print("Invalid input - please guess a letter or a word.")
        
    if guessed: 
        print(f"Good job! {password} is the correct password! 🥳🥳🥳")
        time.sleep(1)
    else:
        print(f"Sorry, you ran out of lives. You lose. 😢😢😢 The password was {password}")
        time.sleep(1)

def main():
    print("""
        H A N G M A N
        Welcome to Hangman. 
        Your job is to guess the password - you can guess single letters one by one, or the whole password at once. You will have 6 attempts. 
        The password might consist of more than one word - if that's the case, there will be no spaces between the words.
        Good luck!!!""")
    password = pick_password()
    play_hangman(password)
    while input("Play again? Y/N: ").upper() == "Y":
        password = pick_password()
        play_hangman(password)

if __name__ == "__main__":
    main()
