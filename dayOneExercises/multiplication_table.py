number = int(input('Enter a number: '))
times = int(input('Enter a times: '))


def multiplication(numbers, x):
    z = 1
    while z <= numbers:
        b = '{} x {} = {}'.format(z, x, x * z)
        print(b)
        z += 1


multiplication(number, times)

