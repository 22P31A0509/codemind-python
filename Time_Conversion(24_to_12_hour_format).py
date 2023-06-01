a=input()
h,m=map(int,a.split(':'))
if h<12:
    p='AM'
else:
    p='PM'
if h%12!=0:
    h=h%12
else:
    h=12
print(f"{h:02d}:{m:02d} {p}")