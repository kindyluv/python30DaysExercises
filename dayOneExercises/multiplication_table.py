number = int(input('Enter a number: '))


def multiplication(numbers):
    z = 0
    while z <= numbers:
        b = '{} x {} = {}'.format(z, z, z * z)
        print(b)
        z += 1


multiplication(number)
