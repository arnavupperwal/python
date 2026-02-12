marks = []
total = 0

for i in range(0,5):
    m =float(input(f"enter grade for subject {i+1}: "))
    marks.append(m)
    total += m

percentage = total / 5
cgpa = percentage / 9.5

if cgpa >= 9 :
    grade = 'A+'
elif cgpa >= 8 :
    grade = 'A'
elif cgpa >= 7 :
    grade = 'B'
elif cgpa >= 6 :
    grade = 'C'
elif cgpa >= 5 :
    grade = 'D'
else:
    grade = 'F'
    
print("-----GRADE SHEET-----")

for i in range(0,5):
    print("Marks obtained in subject ", i+1," = ",marks[i])

print("\nTotal score obtained = ", total)
print("percentage = ", percentage)
print("CGPA = ", cgpa)
print("Grade obtained = ", grade)
