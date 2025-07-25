n=int(input("Enter how many number you want to enter "))
a=[]
for i in range(n):
    b=int(input('Enter the numbers : '))
    a.append(b)


# for maximum numbers 
max=a[0]
min=a[0]

for i in a:
    if max<i:
        max=i
    if min>i:
        min=i

print(f'maximumn number = {max} \nminimum number = {min}')
# sorting numbers

for i in range(len(a)):
    for j in range(len(a)-1):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print(f'the sorted elements are {a}')
# unique elements 
new_list=[]
for i in a:
    if i not in new_list:
        new_list.append(i)
print(f'unique elments = {new_list}')
