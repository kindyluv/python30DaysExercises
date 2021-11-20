from click import prompt
from pexpect.replwrap import python

print(2 + 3)  # addition(+)
print(3 - 1)  # subtraction(-)
print(2 * 3)  # multiplication(*)
print(3 / 2)  # division(/)
print(3 ** 2)  # exponential(**)
print(3 % 2)  # modulus(%)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))  # Int
print(type(3.14))  # Float
print(type(1 + 3j))  # Complex
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))  # List
print(type({'name': 'Asabeneh'}))  # Dictionary
print(type({9.8, 3.14, 2.7}))  # Set
print(type((9.8, 3.14, 2.7)))  # Tuple

print(len('python'), len('dragon'))

# Calculate the number of seconds a person can live

age = int(input('Enter your age: '))

secondsLived = 365 * 24 * 60 * 60

years = age * secondsLived

formatted_string = 'you have lived {}. seconds'.format(years)

print(formatted_string)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b))  # limits it to two digits after decimal
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# unpacking characters
language = 'Python'
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n
