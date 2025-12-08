# 1. Create a set with values {1, 2, 3, 4} .
s={1,2,3,4}
print(s)
#2. Add the value 5 to the set {1, 2, 3, 4} using a set method.
s1={1, 2, 3, 4}
s1.add(5)
print(s1)
#3. Remove the value 3 from the set {1, 2, 3, 4} using a set method.
s2={1, 2, 3, 4}
s2.remove(3)
print(s2)
#4. Check if 2 exists in the set {1, 2, 3, 4} .
s3={1, 2, 3, 4}
print(2 in s3)
#5.Convert the list [1, 2, 2, 3, 4, 4] into a set to remove duplicates.
l=[1, 2, 2, 3, 4, 4]
new=set([1, 2, 2, 3, 4, 4])
print(new)
#6. Convert the tuple (10, 20, 30) into a set.
t=(10, 20, 30)
new_s=set((10,20,30))
print(new_s)
#7.Find the union of sets {1, 2, 3} and {3, 4, 5} .
se1={1, 2, 3}
se2={3, 4, 5}
un=se1.union(se2)
print("Union:",un)
#8.Find the intersection of sets {1, 2, 3} and {3, 4, 5} .
se1={1, 2, 3}
se2={3, 4, 5}
un=se1 & se2
print("Intersection:",un)
#9.Find the difference between sets {1, 2, 3, 4} and {3, 4} .
a= {1, 2, 3, 4}
b={3, 4}
res=a-b
print("Difference:",res)
#10.Create a copy of the set {5, 6, 7} using a set method.
myset={5, 6, 7} 
myset.copy()
print("Copy:",myset)
#11.Remove all elements from the set {1, 2, 3} using one set method
c={1, 2, 3}
c.clear()
print(c)
#12. Check whether {1, 2} is a subset of {1, 2, 3} .
myset1={1, 2}
myset2={1,2,3}
print(myset1.issubset(myset2))
#13.Check whether {1, 2, 3} is a superset of {1, 2} .
my1={1, 2, 3}
my2={1, 2}
print(my1.issuperset(my2))
#14. Find the symmetric difference between {1, 2, 3} and {3, 4, 5} .
x={1, 2, 3}
y={3, 4, 5} 
symmetry=x^y
print("Symmetric Difference:",symmetry)
#15.Add multiple elements {8, 9, 10} into {1, 2, 3} using a set method.
ad={1, 2, 3}
ad.update([8,9,10])
print(ad)
#16. Remove a random element from the set {1, 2, 3} using a set method.
my_set3={1,2,3}
removed=my_set3.pop()
print("Popped item:",removed)
print(my_set3)
#17.Check if two sets {1, 2, 3} and {3, 2, 1} are equal.
checkset1={1,2,3}
checkset2={3,2,1}
print(checkset1==checkset2)
#18.From the list [1, 2, 2, 3, 4, 4, 5] , extract only unique values using a set.
li=[1, 2, 2, 3, 4, 4, 5]
ss=set(li)
print("Unique values of set:",ss)
#19.Convert the set {1, 2, 3} into a list.
s4={1,2,3}
listt=list(s4)
print(listt)  
#20.From {1, 2, 3, 4, 5} , remove {2, 4} using a set method
neww_set={1, 2, 3, 4, 5}
remove_set={2,4}
diff=neww_set-remove_set
print(diff)