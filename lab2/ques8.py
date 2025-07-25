# 8. Write a program to input two sets of student roll numbers: one who play cricket and
# another who play football. Find:
# a. Students who play both sports
# b. Students who play only one sport
# c. Students who play neither (given a master list of all students)
s_football={1,2,3,4,5,6,}
s_cricket={3,4,5,6,7,8}
whole_class=set(range(1,11))
both=s_football&s_cricket
print(f" The sport who play both sport {both}")
print(f"sport who play football only {s_football-s_cricket} sport who play circket only {s_cricket-s_football}")
print(f"the totel number of studen who play only one game {(s_football.union(s_cricket))-both}")
print(f'the students who play neither of the games are {whole_class-(s_football.union(s_cricket))}')
