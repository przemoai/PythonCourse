import datetime

date = datetime.datetime.now()
dateDay=date.strftime("%w")
print(dateDay)


if (dateDay=='0'):
    print("pon")
elif(dateDay=='1'):
    print("wt")
elif(dateDay=='2'):
    print("sr")
elif(dateDay=='3'):
    print("czw")
elif(dateDay=='4'):
    print("pt")
elif(dateDay=='5'):
    print("sb")
elif(dateDay=='6'):
    print("nd")
