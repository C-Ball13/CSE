import random
Rounds = 1
BestRound = 1
money = 35
MostMoney = money

while money > 0:
    if MostMoney < money:
        MostMoney = money
        BestRound = Rounds
    Rounds = (Rounds + 1)
    print("You currently have %d dollars" % money)
    FirstDice = (random.randint(1, 6))
    SecondDice = (random.randint(1, 6))
    print("The First dice is %d" % FirstDice)
    print("The Send Dice is %d" % SecondDice)
    Adding = (FirstDice + SecondDice)
    if Adding is 7:
        print("You won and got some money")
        money = (money + 5)
        print(money)
    else:
        print("You Lost")
        money = money - 1
        print(money)
print("Thank you for your money come again")
print("You should've stopped at round %d when you had %d Dollars" % (BestRound, MostMoney))
