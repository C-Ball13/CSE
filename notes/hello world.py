"""
print("Hello World")

# This is comment. This has no effect on the code
# but this does allow me to do things. I can:
# 1. Make notes to myself
# 2. Comment pieces of code that do not work
# 3. Make my code easier to read

print("Look at what happens here. Is there any space?")
print()
print()
print("There should be a couple blank lines here.")

# Math
print(3 + 5)
print(5 - 2)
print(3 * 4)
print(6 / 2)

print("Figure this out..")
print(6 // 2)
print(5 // 2)
print(9 // 4)

print("Here is another one")
print(6 % 2)
print(5 % 2)
print(11 % 4)     # Modulus (Remainder)

# Powers
# Whats is 2^100
print(2 ** 100)

# taking input
name = input ("What is your name?")
print ("Hello %s." % name)

age = input ("How old are you ? > _")
print ("%s?!? You belong in a museum." % age)
print()
print("#s is really old. They are %s years old." % (age,name))

# Variable Assignments
car_name = "Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 16
car_mile_per_gallon = 0.01

#Make it point. "I have acar called WiebeMobile. It is a Tesla."
print("I have a car called %s. It is %s" % (car_name, car_type))

# Recasting
real_age = int(input ("How old are you again?"))
hidden_age = real_age + 5
print("This your age : %d" % hidden_age)
"""

"""
This is a muti-line comment 
Anything Between this "s is not run.
"""



#Functions
def say_it():
    print("Hello World!")

say_it()
say_it()
say_it()


# f(x)= 2x + 3
def f(x):
    print(2*x + 3)


f(1)
f(5)
f(5000)
"""
# Distance Formula
def distance(x1 y1, x2, y2):
    dist = ((x1-x2)**2 + (y2-y1)**2)(1/2)
    print(dist)


    distance(0, 0, 3, 4)
    distance(0, 0, 5, 12)
"""
"""
# Loops
for i in range (10000):  #This gives the number 0 through 4
    say_it()

for i in range (10)
    print(i+ 1)

    for i in range (5):
        f(i)
"""
# While Loops
a = 1
while a < 10:
    print (a)
    a %= 2   # This is the same as saying a = a + 1

"""
At the moement START the loop:
For loops - Use when how many  you know EXACTLY iterations 
While Loops - Use when you DON'T how many iteration
"""

# Control Structure (If Statement)
sunny = False
if sunny:
    print("Go outside ")



def grade_calc(percentage):
    if precentage >= 90 :
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
         return 'C'
    elif percentage >= 60:
        return "D"
    else:
        return "F"

your_grade = grade_calc(82)
print(your_grade)


    #"Random" NOtes
    import random  # This should be on line 1
    print(random.randint (0, 100))