import random
import sys


# lets set some variables
wordList = [
    "Kendrick Lamar", "Landon Collins", "Jalen Ramsey", "JCole", "A Boogie", "EHS", "A.J. Bouye", "BoonDocks"
           ]

guess_word = []
secretWord = random.choice(wordList)
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []


def beginning():
    print("Hello Player\n")

    while True:
        name = input("Please enter Your name\n").strip()

        if name == '':
            print("You can't do that! No blank lines")
        else:
            break


beginning()


def newfunc():
    print("Well, that's perfect moment to play some Hangman!\n")

    while True:
        gamechoice = input("Would You like to play?\n").upper()

        if gamechoice == "YES" or gamechoice == "Y":
            break
        elif gamechoice == "NO" or gamechoice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue
    newFunc()


def change():
    for character in secretWord: # printing blanks for each letter in secret word
        guess_word.append("-")
    print("Ok, so the word You need to guess has", length_word, "characters")
    print("Be aware that You can enter only 1 letter from a-z\n\n")
    print(guess_word)


def guessing():
    guess_taken = 1
    while guess_taken < 10:
        guess = input("Pick a letter\n").lower()
        if not guess in alphabet:
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage:
            print("You have already guessed that letter!")
        else:

            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                       print(" Sorry Mate, You lost :<! The secret word was",         secretWord)


change()
guessing()

print("Game Over!")