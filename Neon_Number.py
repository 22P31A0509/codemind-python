n=int(input())
a=n*n
p=str(a)
c=0
for i in p:
    i=int(i)
    c+=i

if(n==c):
    print("Neon Number")
else:
    print("Not Neon Number")