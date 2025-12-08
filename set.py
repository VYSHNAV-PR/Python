# my_set={"apple","banana","chery"}
# print(my_set)

#create set using set function
# another_set=set([3,4,5])
# print(another_set)

#accessing item from set using in
# set1={"vyshnav","hari","karthik"}
# print("hari" in set1)

#null set
# set2=set()
# print(set2)

#add items to set .add
# sett={3,4,5,6}
# sett.add(7)
# print(sett)

#.update
# sett={3,4,5,6}
# sett.update([8,9])
# print(sett)

#removing items .remove
# myset={1,2,3,4,5}
# myset.remove(4)
# print(myset)

#.discard   
# myset={1,2,3,4,5}
# myset.discard(4)
# print(myset)

#pop
# myset={1,2,3,4,5}
# myset.pop()
# print(myset)

#clear
# myset={1,2,3,4,5}
# myset.clear()
# print(myset)

#joining the sets
#union
set1={1,2}
set2={3,4}
res=set1.union(set2)
print("Sets after union:",res)

#intersection
sett1={1,2,3}
sett2={2,3,4}
res1=sett1 & sett2
print("Sets after Interection:",res1)

#set difference
sett1={1,2,3}
sett2={2,3,4}
result=sett1 - sett2
print("Sets after Difference:",result)

#set symmetric difference
sett1={1,2,3}
sett2={2,3,4}
result=sett1 ^ sett2
print("Sets after Symmetric Difference:",result)
#copy method
s={2,3,4}
s.copy()
print(s)
#subset
s1={1,2}
s2={1,2,3,4}
print(s1.issubset(s2))
#superset
s1={1,2}
s2={1,2,3,4}
print(s1.issuperset(s2))
#frozen set
s3=frozenset([1,2,3,4,5])
print(s3)