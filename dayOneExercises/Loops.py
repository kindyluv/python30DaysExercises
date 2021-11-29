# loop through a tuples
numbers = (0, 1, 2, 3, 4, 5)

for i in range(len(numbers)):
    print(numbers[i], end=' ' + '\n')

for i in numbers:
    print(i, end=' ' + '\n')

count = 0
while len(numbers) > count:
    print(numbers[count])
    count += 1

# loop though a set
number = {0, 1, 2, 3, 4, 5}
while len(number) > 0:
    print(number)
    break

for i in number:
    print(number)
    break

# loop using
numb = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numb in range(0, 10, 2):
    print(numb)

# nested for loop
person = {
    'first_name': 'Lois',
    'last_name': 'Kindy',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for i in person['skills']:
    print(i)
    for j in person['address']:
        print(j)
        break

list_ = [1, 2, 3, 4, 5]
for i in list_:
    print('#' * i)
