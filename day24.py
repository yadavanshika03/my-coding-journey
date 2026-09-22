tup=(1,2,3,14,34,43)
#tup[0314]
print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
print(tup[3])

if 3 in tup:
	print("yes 3 is present in this tuple")
tup2=tup[1:4]
print(tup2)