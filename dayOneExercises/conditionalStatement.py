language = 'Python'
for letter in language:
    print(letter, end=', ')

for i in range(len(language)):
    print(language[i], end='')

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)  # this way we get both keys and values printed out
