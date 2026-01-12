n=int(input("Enter the size of array:"))
print(f"Enter {n} Elements:")
arr=list(map(int,input().split()))
even_number=[]
odd_number=[]
even_sum=0
odd_sum=0
for num in arr:
    if num%2==0:
        even_number.append(num)
        even_sum+=num
    else:
        odd_number.append(num)
        odd_sum+=num
print(f"Largest element:",max(arr))
print(f"Smallest element:",min(arr))
print(f"Sum of all elements:",sum(arr))
print(f"even numbers:",even_number)
print(f"odd numbers:",odd_number)
print(f"count of even numbers:",len(even_number))
print(f"count of odd numbers:",len(odd_number))
print(f"sum of even number:",sum(even_number))
print(f"sum of odd numbers:",sum(odd_number))
