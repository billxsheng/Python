# A tuple is a sequence of immutable Python objects, a list is also a sequence
# Tuples cannot be changed and use parentheses

tup1 = (1,2,3);
tupEmpty = ();
tupOneVariable = (50,);
print(tup1[0])

tupCombined = tup1 + tupOneVariable
for x in tupCombined: print(x)

print (tup1)