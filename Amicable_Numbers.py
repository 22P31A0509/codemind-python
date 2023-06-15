m=int(input())
n=int(input())
c=0
d=0
for i in range(1,(m//2)+1,1):
    if m%i==0:
        c+=i
for i in range(1,(n//2)+1,1):
    if n%i==0:
        d+=i
if m==d and n==c:
    print("Amicable")
else:
    print("Not Amicable")