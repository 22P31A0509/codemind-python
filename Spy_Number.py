n=int(input())
p=str(n)
c=0
q=1
for i in p:
    i=int(i)
    c+=i
    q*=i
if(c==q):
    print("Spy Number")
else:
    print("Not Spy Number")