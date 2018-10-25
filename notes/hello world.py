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
print("#s is really old. They are %s years old." % (name,age))

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
