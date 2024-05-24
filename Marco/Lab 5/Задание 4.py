def reverse(dict_items):
    reversed = {value: key for key, value in dict_items}
    return reversed


dictionary = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g'}
some = dictionary.items()
r_d = reverse(some)

print(r_d)
