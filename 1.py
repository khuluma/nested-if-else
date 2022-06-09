a=int(input("enter number"))
if a%4==0:
    if a%100!=0 or a%400==0:
        print("leave year")
    else:
        print("not leave year")
else:
    print("simple year")