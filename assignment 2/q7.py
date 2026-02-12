date = int(input("enter the date: "))
month = int(input("enter the month: "))
year = int(input("enter the year: "))

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_month[1] = 29

date +=1

if date > days_in_month[month-1]:
    date = 1
    month +=1
    if month > 12:
        year += 1
        month =1

print("Next date is: ",date,'/',month,'/',year)
