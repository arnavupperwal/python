a = int(input("enter time in seconds: "))

h = a//3600
m = (a % 3600) // 60
s = a % 60

print("hours: " ,h ," ,minutes: " ,m ," ,seconds: " ,s)
