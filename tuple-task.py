#1. Create a tuple (1,2,3,4) and access the element 3 using indexing.
t=(1,2,3,4)
print(t)
my_t=t[2]
print(my_t)
#2. Convert the tuple (10,20,30) into a list.
my_tuple=(10,20,30)
my_list=list(my_tuple)
print(my_list)
#3. Convert the list [1,2,3] into a tuple.
my_li=[1,2,3]
my_tu=tuple(my_li)
print(my_tu)
#4.From the tuple ("a","b","c","d") , extract ("b","c") using slicing
a=("a","b","c","d") 
print(str(a[1:3]).replace("'",'"'))
#5.Check if "x" exists inside the tuple ("x","y","z") .
f=("x","y","z")
pos=f.index("x")
print("Found in",pos,"th position")
#6 Given (5,3,9,1) , find the maximum value using a tuple function
d=(5,3,9,1)
li=list(d)
li.sort()
dd=tuple(li)
print(dd[-1])
#7.Given (1,2,3) , create a new tuple (1,2,3,1,2,3) using tuple operations only.
t1=(1,2,3)
new_t1=t1*2
print(new_t1)
#8.Count how many times 2 appears in (1,2,2,3,2) using a tuple method.
t2=(1,2,2,3,2)
print(t2.count(2),"Times")
#9.Find the index of "cat" in ("dog","cat","mouse")
animal=("dog","cat","mouse")
print(animal.index("cat"))
#10.Reverse (1,2,3,4,5) using slicing.
rev=(1,2,3,4,5)
print(rev[::-1])
#11.Combine (1,2) and (3,4) into (1,2,3,4) using tuple operations.
tuple1=(1,2)
tuple2=(3,4)
joined_tuple=tuple1+tuple2
print(joined_tuple)
#12. Convert "hello" into a tuple of characters
s="hello"
tt=tuple(s)
print(tt)
#13.Convert (1,2,3,4) into the list [1,4] by extracting only first & last elements.
extract=(1,2,3,4)
print(extract[0:4:3])
#14.Given a tuple (10,20,30,40) , replace the value 30 with 99 (hint: convert to list→ modify → convert back).
new=(10,20,30,40) 
lists=list(new)
lists[2]=99
neww=tuple(lists)
print(neww)
#15. Using unpacking, extract a=1 , b=2 , c=3 from (1,2,3) .
unpack=(1,2,3) 
(m,n,o)=unpack
print(m)
print(n)
print(o)
#16.. Create a nested tuple: turn (1,2,3) into ((1,2,3),) .
tupple= (1,2,3)
tupple2=(tupple,)
print(tupple2)
#17. Merge ("a","b") with ["c","d"] to get a single tuple ("a","b","c","d") (hint: convert list→ tuple).
one=("a","b")
two=["c","d"]
three=tuple(two)
joinn=one+three
print(str(joinn).replace("'",'"'))
#18.Check if tuple (1,2,3) is equal to its reverse.
one_t=(1,2,3)
print(one_t[::-1]==t)
#19.Convert a tuple of lists ([1,2],[3,4]) into a single flat list [1,2,3,4] .
tuplee= ([1,2],[3,4])
print(tuplee[0]+tuplee[1])
#20.Given (1, [2,3], 4) , add 5 inside the inner list so result becomes (1, [2,3,5], 4) .
my_newtuple=(1, [2,3], 4)
my_newtuple[1].append(5)
print(my_newtuple)