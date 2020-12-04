import random

random_int = random.randint(1, 10)
print(random_int)

random_float = random.random() * 100
print(round(random_float, 2))

love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')

test_seed = int(input('Create a seed number: '))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 1:
    print('Heads')
else:
    print('Tails')
