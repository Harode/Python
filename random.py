import random

mylist = list(range(0,20))

print (mylist)

random.choices(population=mylist,k=10)
#print(random.choices(popluation=mylist, k=10))
