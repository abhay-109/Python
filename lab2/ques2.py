l1=[1,2,34,4,5]
l2=[3,4,5,6]
merge_list=l1+l2
print(merge_list)
print(set(merge_list)-(set(l1)&set(l2)))
