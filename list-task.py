#1. Create a list [1,2,3] and add 4 to the end using a list method
a=[1,2,3]
a.append(4)
print(a)
 #2. Given [10,20,30] , remove 20 using a list method.
b=[10,20,30]
b.pop(1)
print(b)
#3. From [5,3,9,1] , sort the list in ascending order using a list method.
c=[5,3,9,1]
c.sort()
print(c)
#4. From [1,2,3,4,5] , extract [2,3,4] using slicing only
d=[1,2,3,4,5]
print(d[1:4])
#5. Reverse the list [1,2,3,4] using slicing (no loops).
l=[1,2,3,4] 
print(l[::-1])
#6. Combine [1,2] and [3,4] into one list using list operations
l1=[1,2]
l2=[3,4]
joined=l1+l2
print(joined)
#7.Convert [7,8] into [7,8,7,8] using list operations.
li=[7,8]
j=li+li
print(j)
# 8.Check if 3 exists in [1,2,3,4] using a list operator.
f=[1,2,3,4]
pos=f.index(3)
print("Found in",pos,"nd position")
#9. Count how many times 2 appears in [1,2,2,3,2] using a list method
g=[1,2,2,3,2]
g_count=g.count(2)
print(g_count,"Times")
#10. Remove the last element from ["a","b","c","d"] using a list method.
lst=["a","b","c","d"] 
lst.pop()
print(lst)
#11. Insert "x" at index 1 in ["a","b","c"] using a list method.
ins=["a","b","c"]
ins.insert(1,"x")
print(ins)
#12.Replace the element at index 2 in [10,20,30,40] with 99 using indexing.
rep=[10,20,30,40]
rep[2]=99
print(rep)
#13.Convert range(5) into a list using list functions
num=list( range(5))
print(num)
#14. Using slicing, extract every 2nd element from [1,2,3,4,5,6] → expected [2,4,6] .
n=[1,2,3,4,5,6]
print(n[1:6:2])
#15.Remove all elements from [1,2,3] using one list method
all=[1,2,3]
all.clear()
print(all)
#16.Copy a list [4,5,6] using only list tools (no modules).
lst1=[4,5,6]
new_lst1=lst1.copy()
print(new_lst1)
#17.Convert [1,2,3] into a nested list [[1,2,3]] using list operations.
lst2=[1,2,3]
new=[lst2]
print(new)
#18. Extend [1,2] with [3,4,5] using a list method.
ex1=[1,2]
ex2=[3,4,5]
ex1.extend(ex2)
print(ex1)
#19.Using list repetition, create a list ["hello","hello","hello"] .
x=["hello"]*3
print(str(x).replace("'",'"'))
#20.Remove the element at index 2 from [10,20,30,40] using a list method
z=[10,20,30,40]
z.pop(2)
print(z)

