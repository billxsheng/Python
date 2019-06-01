import collections

dict1 = {"day1": "Mon", "day2": "Tues"}
dict2 = {"day3": "Wed", "day4": "Thurs"}

map = collections.ChainMap(dict1, dict2)
print(map)
print('Keys = {}'.format(list(map.keys())))
print('Values = {}'.format(list(map.values())))
print()

for key,val in map.items():
    print('{} = {}'.format(key, val))
