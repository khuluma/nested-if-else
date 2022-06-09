age=int(input("enter number"))
sex=input("enter number")
marital=input("are you married")
if sex=="m":
    if age>=20 and age <=40 or marital=="yess":
        print("he work in anywhere")
    elif age>=40 and age<=60 or marital=="yess":
        print(" he wii work only urban area")
    else:
        print("he not married")
elif sex==("f"):
    print("she will work only in urban")
else:
    print("error")
