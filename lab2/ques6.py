l1=[]
num=int(input("enter how many numbers you want to add : "))

for i in range(num):
    i=int(input('Enter the number : '))
    l1.append(i)
tup=tuple(l1)
# average
sum=sum(tup)
print(f"Average : {sum/len(tup)}")
# meadian
if len(tup)%2!=0:
    
    print(f'Median : {tup[int((len(tup)+1)/2)-1]}')
else:
    print(f'Median : {(tup[int((len(tup))/2)-1]+tup[int((len(tup))/2)])/2 }')
# mode
mode={}
uniq=set(l1)
for i in uniq:
    mode[i]=l1.count(i)
keys=list(mode.keys())
values=list(mode.values())
m=max(values)
index_of_max_element=values.index(m)
print(f'the mode of the numbers : {keys[index_of_max_element]}')    


