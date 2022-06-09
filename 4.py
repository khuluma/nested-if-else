day=input("enter day")
meal_time=input("enter meal time")
if day=="monday":
    if meal_time=="breakfast":
        print("pori sabji")
    elif meal_time=="lunch":
        print("sambhar rich")
    elif meal_time=="dinner":
        print("pulav soup")
    else:
        print("no meal")
elif day=="tuesday":
    if meal_time=="breakfast":
        print("sendwitch")
    elif meal_time=="lunch":
        print("alo paratha")
    elif meal_time=="dinner":
        print("roti sobji")
    else:
        print("not meal")
else:
    print("none")