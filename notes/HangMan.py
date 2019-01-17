import random
import string
word = "Odell Bbeckham Jr", "Landon Collins", "Jalen Ramsey", "Lebron James", "Kyrie Ivring", "Allen Inverson", "A.J. Bouye", "Richard Sherman", "Anthony Davis", "Russell Westbrook"

print("Can you figure out the word i'm thinking of")

word = random.choice(word)
print(word)
print(list(string.punctuation))
print(string.whitespace)

