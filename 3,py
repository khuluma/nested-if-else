e_day=int(input("enter expected day"))
e_month=int(input("enter expected month"))
e_year=int(input("enter expected year"))
r_day=int(input("enter return day"))
r_month=int(input("enter return month"))
r_year=int(input("enter return year"))
if e_month==r_month and r_year==e_year:
    if r_day<=e_day:
        print("no find")
    elif r_day>=e_day:
        n_d_late=r_day-e_day
        fine=n_d_late*15
        print("fine",fine)
    else:
        print("fine")
elif r_day>=e_day and r_year==e_year:
    if r_month >= e_month:
        n_d_late=r_day-e_day
        n_m_late=(r_month-e_month)*30
        n_late=n_m_late-n_d_late
        fine=500*n_late
        print("fine",fine)
    else:
        print("fine charge")
elif r_month==e_month and r_day>=e_day:
    if r_year>=e_year:
         fixed_fine=10000
         print("fixed fine",fine)
    else:
        print("no fixed")
else:
    print("error")
