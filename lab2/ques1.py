list1=input("Enter the numbers ").split()
list2=[]
for i in list1:
    list2.append(int(i))
print(f'maximumn number = {max(list1)} \nminimum number = {min(list1)}')
list2.sort()
print(f'sorted list = {list2}')
print(f'unique elments = {list(set(list1))}')
