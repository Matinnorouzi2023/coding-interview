
year = int(input("please tell a year"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("your year is leap")
        else:
            print("your year is no leap")
    else:
        print(" your  year si not leap.")
else:
    print(" your  year si not leap.")