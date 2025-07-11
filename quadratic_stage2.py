import math

# Take input from the user
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

# Calculate the discriminant
discriminant = b ** 2 - 4 * a * c

# Check if roots are real
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    root = -b / (2 * a)
    print("Both roots are equal:", root)
else:
    print("No real roots.")
