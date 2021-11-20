numbers = int(input('Enter a number: '))

i = 1
while i <= numbers:
    print('*' * i)
    i += 1

j = 1
while j <= numbers:
    print('*' * (numbers - j))
    j += 1


def create_pyramid(rows):
    for k in range(rows):
        print((' ' * (rows - k - 1) + '*' * (2 * k + 1)))


print((create_pyramid(numbers)))


def create_upside_down_pyramid(rows):
    for l in reversed(list(range(rows))):
        print((' ' * (rows - l - 1) + '*' * (2 * l + 1)))


print((create_upside_down_pyramid(numbers)))


for t in range(numbers):
    for y in range(numbers):
        print('*', end=' ')
    print()


