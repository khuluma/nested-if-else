a=int(input("enter a number"))
if a<=25:
    print("grade f")
if a>=25 and a<=45:
    print("grade e")
elif a>=45 and a<=50:
    print("grade d")
if a>=50 and a<=60:
    print("grade c")
elif a>=60 and a<=80:
    print("grade b")
if a>=80:
    print("grade a")
else:
    print("no grade")