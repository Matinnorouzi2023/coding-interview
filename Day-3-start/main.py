
print("wellcome to the roller coaster!")
height = int(input("what is your height in cm ?"))
bill = 0
if height >= 120:
    print("you can ride the roller coaster")
    age = int(input("what is your age:"))
    if age <= 12:
        bill = 5
        print(" child tickets pay $5.")
    elif age < 12 <= 18:
        bill = 7
        print(" young tickets should pay $7.")
    else:
        bill = 12
        print(" adult tickets pay $12 .")
    wants_photo = input(" Doy ou want a photo taken? Y or N.")
    if wants_photo == "y":
    #Add $3 to their bill
      bill += 3
    print(f" your final bill is{bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")