a=input()
a1=a.lower()
a2=a1.split()
l=[]
for i in a2:
    for j in i:
        l.append(j)
n=sorted(set(l))
for i in n:
    print(i,end="")