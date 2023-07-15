from random import randint
from time import sleep
List = list()
games = list()
print('-' * 30)
print('            Lottery     ')
print('-' * 30)
quantity = int(input('How many games you want me to raffle? '))
total = 1
while total <= quantity:
    count = 0
    while True:
        numbers = randint(1, 60)
        if numbers not in List:
            List.append(numbers)
            count += 1
        if count >= 6:
            break
    List.sort()
    games.append(List[:])
    List.clear()
    total += 1
print('-=' * 3, f' Drawing lots {quantity} games ', '-=' * 3)
for i, j in enumerate(games):
    print(f'Game {i+1}: {j}')
    sleep(1)
print('-=' * 5, '< GOOD LUCK! >', '-=' * 5)
