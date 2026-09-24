def calculate_bonus_percentage(experience):
    if experience >= 10: return 0.20
    elif experience >= 5: return 0.10
    elif experience >= 2: return 0.05
    else: return 0.0

names = []
departments = []
base_salaries = []
experiences = []
total_salaries = []

n = int(input("Enter the number of employees: "))

for i in range(n):
    print(f"\nEnter details for Employee {i + 1}")
    name = input("Name: ")
    dept = input("Department: ").strip()
    salary = float(input("Base Salary (taka): "))
    exp = float(input("Experience (years): "))

    bonus_rate = calculate_bonus_percentage(exp)
    final_salary = salary * (1 + bonus_rate)

    names.append(name)
    departments.append(dept)
    base_salaries.append(salary)
    experiences.append(exp)
    total_salaries.append(final_salary)

max_salary_idx = total_salaries.index(max(total_salaries))

max_exp_idx = experiences.index(max(experiences))

avg_salary = sum(total_salaries) / len(total_salaries)

senior_it_employees = [
    names[i]
    for i in range(n)
    if departments[i].upper() == "IT" and experiences[i] > 5
]

print()
print(f"{'Name':<25} | {'Dept':<15} | {'Exp (yrs)':<10} | {'Total Salary':<15}")
print("_" * 75)
for i in range(n):
    print(f"{names[i]:<25} | {departments[i]:<15} | {experiences[i]:<10.1f} | taka {total_salaries[i]:<14.2f}")

print()
print(f"Average Salary (Post-Bonus): taka {avg_salary:.2f}")
print(f"Highest-Paid Employee: {names[max_salary_idx]} (taka {total_salaries[max_salary_idx]:.2f})")
print(f"Most Experienced Employee: {names[max_exp_idx]} ({experiences[max_exp_idx]:.1f} years)")

print("IT Employees with > 5 Years Experience: ", end="")
if senior_it_employees: print(", ".join(senior_it_employees))
else: print("None found")