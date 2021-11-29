lst = ['item', 'item2', 'item3', 'item4', 'item5']
first_item, *rest = lst
print(lst)
print(lst[::2])  # removes all second items from the list
print('item3' in lst)
del lst[2]
print(lst)
