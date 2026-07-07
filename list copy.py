list1=[1,2,3,4,5]
list2=list1  #assiment copy 
print(list2)

list2.append(6)

print(list2)
print(list1)


list2=list1.copy() #shallow copy
print(list2)

list2.append(7)

print(list2)
print(list1)

import copy
list2=copy.deepcopy(list1) #deep copy
print(list2)
