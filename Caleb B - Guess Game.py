number = 5
guesses = 5
win = False

while guesses > 0:
    num = int(input("what's a number from 1 to 10"))
    if num > 11:
        print("That's to high")
        guesses = - 1
    elif num > number:
        print("That's way to low")
        guesses = guesses - 1
    elif num == number:
        print("You got the answer")
        guesses = 0