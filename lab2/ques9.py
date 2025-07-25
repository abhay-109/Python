# 9. Create a set of random numbers. Add more numbers until the set has 10 unique
# elements. Also, remove the smallest and largest element.
import random 
l_random=[]
while True:
    if len(set(l_random))==10:
        break
    num=random.randint(0,100)
    l_random.append(num)
print(l_random)
m=max(l_random)
l_random.remove(m)
min=min(l_random)
l_random.remove(min)
print(f'set afterremoving max and min element {l_random}')
