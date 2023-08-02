a=input().split(";")
space=[0,0]
for i in range(len(a)):
    if len(a[i])<2:
        continue
    elif a[i][0] in ["A","S","W","D"]:
        try:
            x=int(a[i][1:])
            if a[i][0]=="A":
                space[0]-=x
            if a[i][0]=="S":
                space[1]-=x
            if a[i][0]=="W":
                space[1]+=x
            if a[i][0]=="D":
                space[0]+=x
        except:
            continue
print(space[0],end=",")
print(space[1])