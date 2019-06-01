list = ['bill', 'sheng', 1, 2]

list2 = [1,2,3,4,5]

list3 = ['a', 'b', 'c', 'd', 'e']

print ("list0: ", list[0])

# when iterating the second number is < like a for loop
print ("list0: ", list[0:3])

list[1] = 'two'
print(list[0:4])

del list[2]
print(list[0:3])

lista = [1,2,3]
listb = [4,5,6]

# length
print (len(lista))

# concatenation
listc = lista + listb
for x in listc: print(x)

# repetition
listd = ['a'] * 4
for y in listd: print(y)

# membership
print(3 in lista)

# iteration
for x in lista: print(x)