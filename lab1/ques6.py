list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

intersection_set = set1.intersection(set2)

intersection_list = list(intersection_set)

print(intersection_list)

another_list1 = ['apple', 'banana', 'orange', 'grape']
another_list2 = ['banana', 'kiwi', 'orange', 'melon']

another_set1 = set(another_list1)
another_set2 = set(another_list2)

another_intersection_set = another_set1.intersection(another_set2)

another_intersection_list = list(another_intersection_set)

print(another_intersection_list)
