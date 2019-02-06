import random

word_bank = [
    "kendricklamar", "landoncollins", "jalenramsey", "jcole", "aboogie", "ehs", "ajbouye", "boondocks"
           ]

guess_word = []
hiddenWord = random.choice(word_bank)
length_word = len(hiddenWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
word_bank = []


def beginning():
    print("Hello Player")

    while True:
        name = input("Enter Name")

        if name == '':
            print("You can't put nothing.")
        else:
            break


beginning()


def newfunc():
    print("Well, that's perfect moment to play some Hangman!")

    while True:
        choice = input("Would You like to play?").upper()

        if choice == "YES" or choice == "Y":
            break
        elif choice == "NO" or choice == "N":
            exit("That's a shame! Have a nice day")
        else:
            print("Answer with only Yes or No")
        continue


def change():
    for characters in hiddenWord:
        guess_word.append("-")
    print("Ok, so the word You need to guess has", length_word, "characters")


print("Be aware that You can enter only 1 letter from a-z")
print(guess_word)


def guessing():
    guess_taken = 1
    while guess_taken < 10:
        guess = input("Pick a letter").lower()
        if not guess in alphabet:
            print("Enter a letter from a-z alphabet")
        elif guess in word_bank:
            print("You have already guessed that letter Try again!")
        else:

            word_bank.append(guess)
            if guess in hiddenWord:
                print("You Got it!")
                for x in range(0, length_word):
                    if hiddenWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("You won now leave before we take that away!")
                    break
            else:
                print("Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print(" Sorry Man, You lost -_-! The hidden word was",         hiddenWord)


change()
guessing()

print("Game Over!")
