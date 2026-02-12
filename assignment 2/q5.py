import math 

a = float(input("enter coefficient a: "))
b = float(input("enter coefficient b: "))
c = float(input("enter coefficient c: "))

D = b ** 2 - 4 * a * c

if D > 0 :
    root1 = ( -b + math.sqrt(D)) / (2*a)
    root2 = ( -b - math.sqrt(D)) / (2*a)
    print("roots are real and distinct.")
    print("root 1 = ",root1)
    print("root 2 = ",root2)
elif D == 0 :
    root = -b / (2*a)
    print("roots are real and equal.")
    print("root = ",root)
else:
    real_part = -b / (2*a)
    imag_part = math.sqrt(-D) / (2*a)
    print("roots are imaginary.")
    print("root 1 = ", real_part, " + ", imag_part,"i")
    print("root 2 = ", real_part, " - ", imag_part,"i")
