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

items = ['he', 'she', 'me', 'them', 'us', 'then']
A, B, C, D, E, F = items
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
print(items[::-1])
print(items[1:4])

challenge = 'thirty days of python'
print(challenge.count('y'))  # 3
print(challenge.count('y', 7, 14))  # 1,
print(challenge.count('th'))  # 2`
print(challenge.upper())

# expandtabs(): Replaces tab character with spaces,
# default tab size is 8. It takes tab size argument
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())  # 'thirty  days    of      python'
print(challenge.expandtabs(10))  # 'thirty    days      of        python'

# find(): Returns the index of the first occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.find('y'))  # 16
print(challenge.find('th'))  # 17

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 5
print(challenge.rfind('th'))  # 1

# index(): Returns the lowest index of a substring,
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7

#  rindex(): Returns the highest index of a substring,
#  additional arguments indicate starting and ending index (default 0 and string length - 1)

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8

# isalnum(): Checks alphanumeric character
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'thirty days of python'
print(challenge.isalnum())  # False, space is not an alphanumeric character

challenge = 'thirty days of python 2019'
print(challenge.isalnum())  # False

# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
challenge = 'thirty days of python'
print(challenge.isalpha())  # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())  # False

# isalpha(), isalnum(), isdecimal(), isdigit(), isnumeric(), isidentifier(), islower(), isupper()

# strip(): Removes all given characters starting from the beginning and end of the string
challenge = 'thirty days of pythoonnn'
print(challenge.strip('thirty'))  # 'irty days of py'

# join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)  # 'HTML CSS JavaScript React'
