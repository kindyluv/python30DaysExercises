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

# split
challenge = 'thirty days of python'
print(challenge.split())  # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', '))  # ['thirty', 'days', 'of', 'python']
