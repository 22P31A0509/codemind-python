n=int(input())
s=n*n
p=str(n)
q=str(s)
if q.endswith(p):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")