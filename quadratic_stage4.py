import math

# Open the input file
with open("input.txt", "r") as file:
    lines = file.readlines()

# Process each set of a, b, c
for i, line in enumerate(lines):
    a, b, c = map(float, line.strip().split())
    print(f"\nEquation {i+1}: {a}x^2 + {b:+}x + {c:+} = 0")


    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("  Root 1:", root1)
        print("  Root 2:", root2)
    elif discriminant == 0:
        root = -b / (2 * a)
        print("  Both roots are equal:", root)
    else:
        print("  No real roots.")
