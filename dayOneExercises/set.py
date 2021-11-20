
# set

lis1 = [3, 4, 1, 4, 5]

sets = str(set(lis1))
print(sets)

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])
print(st)

#  set Union
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3)

# update set
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)  # st2 contents are added to st1
print(st1)

# set difference
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
dif = whole_numbers.difference(even_numbers)  # {1, 3, 5, 7, 9}
print(dif)

python_ = {'p', 'y', 't', 'o', 'n'}
dragon_ = {'d', 'r', 'a', 'g', 'o', 'n'}
python_.difference(dragon_)  # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
ani = dragon_.difference(python_)  # {'d', 'r', 'a', 'g'}
print(ani)

# set intersection
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
intersection = whole_numbers.intersection(even_numbers)  # {0, 2, 4, 6, 8, 10}
print(intersection)

python__ = {'p', 'y', 't', 'h', 'o', 'n'}
dragon__ = {'d', 'r', 'a', 'g', 'o', 'n'}
ints = python__.intersection(dragon__)  # {'o', 'n'}
print(ints)

#  is_subset and is_superset
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers)  # False, because it is a super set
print(whole_numbers.issuperset(even_numbers))  # True

python1 = {'p', 'y', 't', 'h', 'o', 'n'}
dragon1 = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python1.issubset(dragon1))  # False

# set symmetric_difference
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers)  # {0, 6, 7, 8, 9, 10}

python2 = {'p', 'y', 't', 'h', 'o', 'n'}
dragon2 = {'d', 'r', 'a', 'g', 'o', 'n'}
print(python2.symmetric_difference(dragon2))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}

# disjoint() is two items with no similar items in them
even_numbers = {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers))  # True, because no common item

python3 = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'a', 'g', 'o', 'n'}
python3.isdisjoint(dragon)  # False, there are common items {'o', 'n'}
