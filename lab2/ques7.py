# Write a program that receives a list of tuples representing (x, y) coordinates. Determine
# whether the points form a straight line.
points=[]
for i in range(3):
    print(f"Point {i+1}")
    x=int(input("x : "))
    y=int(input("y : "))
    points.append([x,y])
if (((points[1][1]-points[0][1])/(points[1][0]-points[0][0]))==((points[2][1]-points[0][1])/(points[2][0]-points[0][0]))):
    print('They are coliner ')
else:
    print('They are not coliner ')
    
