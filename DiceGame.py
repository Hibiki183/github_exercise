import random
def RollDice():
    dice = random.randint(1, 6)
    return dice

dice = []

dice.append(RollDice())
dice.append(RollDice())

name = input('What is your name?\n>')
print(f'Hello, {name}!')

print('Rolling the dice...')
for i in range(2):
    print(f'Dice {i + 1}: {dice[i]}')

totalValue = dice[0] + dice[1]

print(f'Total Value: {totalValue}')
