from array import *
# first argument is bytecode and represents what the array will be made of
array = array('i', [1,2,3,4,5])
for x in array: print(x)

print(array[0])

array.insert(1, 60)
for y in array: print(y)

array.remove(60)
for x in array: print(x)

print(array.index(5))

array[4] = 60

for x in array: print(x)
