user_input=[]
num=int(input("Enter the how many numbers you want to add : "))
result=[]
for i in range(num):
    i=int(input('enter the number : '))
    user_input.append(i)

for id,i in enumerate(user_input):
    if id%2==0:
        prim=True
        if i>1:
            for i in range(2,int(i**(1/2))+1):
                prim=False
                break
        else:
            prim=False
        if prim:
            result.append(i)

print(result)
