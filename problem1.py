names = []
sub1_marks = []
sub2_marks = []
sub3_marks = []
totals = []
averages = []
grades = []

n = int(input("Enter the number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i + 1}")
    name = input("Name: ")
    m1 = float(input("Subject 1 Marks: "))
    m2 = float(input("Subject 2 Marks: "))
    m3 = float(input("Subject 3 Marks: "))

    total = m1 + m2 + m3
    avg = total / 3

    if avg >= 80: grade = "A+"
    elif avg >= 70: grade = "A"
    elif avg >= 60: grade = "B"
    elif avg >= 50: grade = "C"
    elif avg >= 40: grade = "D"
    else: grade = "F"

    names.append(name)
    sub1_marks.append(m1)
    sub2_marks.append(m2)
    sub3_marks.append(m3)
    totals.append(total)
    averages.append(avg)
    grades.append(grade)

highest_idx = totals.index(max(totals))
lowest_idx = totals.index(min(totals))

passed_count = 0
failed_count = 0
a_plus_students = []

for idx in range(n):
    if grades[idx] == "F": failed_count += 1
    else: passed_count += 1

    if grades[idx] == "A+": a_plus_students.append(names[idx])

print(f"{'Name':<25} | {'Total':<8} | {'Average':<8} | {'Grade':<6}")
print("_" * 70)
for idx in range(n):
    print(f"{names[idx]:<25} | {totals[idx]:<8.2f} | {averages[idx]:<8.2f} | {grades[idx]:<6}")
print(f"Highest Scorer: {names[highest_idx]} (Total: {totals[highest_idx]:.2f}, Avg: {averages[highest_idx]:.2f})")
print(f"Lowest Scorer:  {names[lowest_idx]} (Total: {totals[lowest_idx]:.2f}, Avg: {averages[lowest_idx]:.2f})")
print(f"Passed Students: {passed_count}")
print(f"Failed Students: {failed_count}")

print("Students with A+ Grade: ", end="")
if a_plus_students: print(", ".join(a_plus_students))
else: print("None")