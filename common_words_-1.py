a=input()
b=input()
a1=a.lower()
b1=b.lower()
a2=a1.split()
b2=b1.split()
c=0
for i in a2:
    if i in b2:
        c+=1
print(c)