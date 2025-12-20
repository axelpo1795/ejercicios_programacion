#Ejercicio5_S4
n = int(input("How many grades do you want to enter? "))

grades = []
for i in range(n):
    grade = float(input(f"Enter grade #{i + 1}: "))
    grades.append(grade)

approved = []
failed = []

for grade in grades:
    if grade >= 70:
        approved.append(grade)
    else:
        failed.append(grade)

# Calcular promedios
average_all = sum(grades) / len(grades)

if len(approved) > 0:
    average_approved = sum(approved) / len(approved)
else:
    average_approved = 0

if len(failed) > 0:
    average_failed = sum(failed) / len(failed)
else:
    average_failed = 0

print(f"\nApproved grades: {len(approved)}")
print(f"Failed grades: {len(failed)}")
print(f"Overall average: {average_all:.2f}")
print(f"Approved average: {average_approved:.2f}")
print(f"Failed average: {average_failed:.2f}")