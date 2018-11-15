import random
Rounds = 1
BestRound = 1
money = 35
MostMoney = Money

while money > 0:
    if MostMoney < money:
        MostMoney = money
        BestRound = Rounds
    Rounds = (Rounds + 1)
    print("yYou currently have %d dollars" % money)
    FirstDice = random.randint (1,6)
    SecondDice = random.randint (1,6)
    print("The First dice is %d" % FirstDice)
    print()
