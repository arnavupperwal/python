year = int(input("enter any year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("given year is a leap year.")
else:
    print("given year is not a leap year.")
