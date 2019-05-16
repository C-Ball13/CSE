import random
import sys


# lets set some variables
wordbank = [
    "kendricklamar", "landoncollins", "jalenramsey", "jcole", "aboogie", "ehs", "ajbouye", "boondocks"
           ]

guess_word = []
hiddenWord = random.choice(wordbank)
length_word = len(hiddenWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
wordbank = []

next_room = player.find_room(command)
            player.move(next_room)
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
            print("Answer with only  Yes or No")
        continue


def change():
    for character in hiddenWord:  # printing blanks for each letter in secret word
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
        elif guess in wordbank:
            print("You have already guessed that letter!")
        else:

            wordbank.append(guess)
            if guess in hiddenWord:
                print("You Got it!")
                for x in range(0, length_word):
                    if hiddenWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print(" Sorry Man, You lost -_-! The hidden word was",         hiddenWord)


change()
guessing()

print("Game Over!")
