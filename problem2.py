num = []

input = input("\nPlease enter 20 integers: ")
num = [int(x) for x in input.split()]

# Initialize storage lists and counters
even_numbers = []
odd_numbers = []
even_squares = []
odd_cubes = []

positive_count = 0
negative_count = 0
zero_count = 0

# Process each number in the list
for x in num:
    # Check even or odd
    if x % 2 == 0:
        even_numbers.append(x)
        even_squares.append(x**2)
    else:
        odd_numbers.append(x)
        odd_cubes.append(x**3)

    # Check positive, negative, or zero
    if x > 0:
        positive_count += 1
    elif x < 0:
        negative_count += 1
    else:
        zero_count += 1

# Display Results
# print("\n" + "=" * 45)
# print("RESULTS SUMMARY")
# print("=" * 45)

print(f"\nOriginal List: {num}\n")

print(f"Even Numbers: {even_numbers}")
print(f"Sum of Even Numbers: {sum(even_numbers)}")
print(f"Squares of Even Numbers: {even_squares}")

print(f"Odd Numbers: {odd_numbers}")
print(f"Sum of Odd Numbers: {sum(odd_numbers)}")
print(f"Cubes of Odd Numbers: {odd_cubes}")

print(f"Largest Number: {max(num)}")
print(f"Smallest Number: {min(num)}")

print("Value Counts:")
print(f"  - Positive Numbers: {positive_count}")
print(f"  - Negative Numbers: {negative_count}")
print(f"  - Zeroes: {zero_count}")

"""
1 -2 3 -4 5 6 -7 8 9 0 11 -12 13 14 -15 16 17 -18 19 0

-1 -3 -5 -7 -9 -11 -13 -15 -17 -19 0 0 0 0 0 -21 -23 -25 -27 -29
"""