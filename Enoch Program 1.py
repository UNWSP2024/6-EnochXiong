import random

def randDice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2

total = 0

for i in range(100):
    total += randDice()

average = total / 100

print("Average of 100 rolls:", round(average, 2))
