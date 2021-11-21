import string
from random import random, randint


print(string.ascii_letters)  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)  # 0123456789
print(string.punctuation)  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


print(random())  # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20))  # it returns a random integer number between [5, 20] inclusive
