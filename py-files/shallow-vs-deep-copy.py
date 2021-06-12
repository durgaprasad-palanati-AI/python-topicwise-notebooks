list1=[10,20,30]
print("list1=",list1)
#shallow copy
list2=list1.copy()
print("after shallow copy")
print("list2=",list2)
print("addrress of list1=",hex(id(list1)))
print("addrress of list2=",hex(id(list2)))


print("addrress of list1[0]=",hex(id(list1[0])))
print("addrress of list2[0]=",hex(id(list2[0])))


del list1
del list2

print("----------------------------")
import copy


list1=[10,20,30]
print("list1=",list1)
#deep copy
list2=copy.deepcopy(list1)
print("after deep copy")
print("list2=",list2)
print("addrress of list1=",hex(id(list1)))
print("addrress of list2=",hex(id(list2)))



print("addrress of list1[0]=",hex(id(list1[0])))
print("addrress of list2[0]=",hex(id(list2[0])))
list2[0]=40
print("list2[0]=",list2[0],"addrress of list2[0]=",hex(id(list2[0])))
del list1
del list2

print("----------------------------")

list1=[10,20,30]
print("list1=",list1)
#deep copy
list2=copy.copy(list1)
print("after shallow copy")
print("list2=",list2)
print("addrress of list1=",hex(id(list1)))
print("addrress of list2=",hex(id(list2)))

print("addrress of list1[0]=",hex(id(list1[0])))
print("addrress of list2[0]=",hex(id(list2[0])))

list2[0]=40
print("list2[0]=",list2[0],"addrress of list2[0]=",hex(id(list2[0])))

del list1
del list2
