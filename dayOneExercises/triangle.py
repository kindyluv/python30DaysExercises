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
    for i in range(rows):
        print((' ' * (rows - i - 1) + '*' * (2 * i + 1)))


print((create_pyramid(numbers)))


def create_upside_down_pyramid(rows):
    for i in reversed(list(range(rows))):
        print((' ' * (rows - i - 1) + '*' * (2 * i + 1)))


print((create_upside_down_pyramid(numbers)))
