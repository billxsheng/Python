days = set([0,1,2,3,4,5,6])
print(days)

days.add(7)
print(days)

days.discard(5)
print(days)

days2 = set([1, 60])

union = days|days2
print(union)

intersection = days & days2
print(intersection)

difference = days - days2
print(difference)

# check if given set is a subset or superset of another set
set1 = set([1,2,3,4])
set2 = set([1,2])
subset = set1 <= set2
subset2 = set2 <= set1
superset = set1 >= set2

print(subset)
print(subset2)
print(superset)