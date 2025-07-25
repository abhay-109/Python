l1='what are you doing doing'
l2=l1.split()
u_elements=list(set(l2))
new_list=[]
for i in u_elements:
    new_list.append(f"{i} : {l2.count(i)}")
print(new_list)
