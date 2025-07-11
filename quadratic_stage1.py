import math

# Hardcoded values for a, b, and c
a = 1
b = -3
c = 2

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
