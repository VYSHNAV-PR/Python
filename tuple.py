tuple1=('apple',)
print(tuple1)

my_tuple=('apple','banana','cherry','grapes','orange')
print(my_tuple[0])
#slicing
print(my_tuple[1:3])

#updating tuple
#tuple-list
my_list=('apple','banana','cherry','grapes','orange')
temp_list=list(my_list)
temp_list[2]='pineapple'
my_list=tuple(temp_list)
print(my_list)

#unpacking tuple
fruits=('apple','banana','cherry')
(fruit1,fruit2,fruit3)=fruits
print(fruit1)
print(fruit2)
print(fruit3)
#Using * (asterisk)
fruit_s=('apple','banana','cherry','orange')
(fruit_one,*fruit_two,fruit_three)=fruit_s
print(fruit_one)
print(fruit_two)
print(fruit_three)

#joining tuple
t1=(10,20,30)
t2=(40,50,60)
joined=t1+t2
print(joined)

#tuple method-count
t=(1,2,3,3,4,2)
print(t.count(2))
