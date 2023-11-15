#Roots Of Quadratic Equations
import cmath

# Coefficients of the quadratic equation: ax^2 + bx + c = 0
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Calculate the roots
root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
root2 = (-b - cmath.sqrt(discriminant)) / (2*a)

# Display the roots
print(f"Root 1: {root1}")
print(f"Root 2: {root2}")



# Another Method
# import math

# def quadratic_roots(a, b, c):
#     discriminant = b**2 - 4*a*c
#     if discriminant > 0:
#         root1 = (-b + math.sqrt(discriminant)) / (2*a)
#         root2 = (-b - math.sqrt(discriminant)) / (2*a)
#         return root1, root2
#     elif discriminant == 0:
#         root = -b / (2*a)
#         return root, root
#     else:
#         real_part = -b / (2*a)
#         imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
#         return f"{real_part} + {imaginary_part}i", f"{real_part} - {imaginary_part}i"

# # Input coefficients a, b, c
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))

# # Calculate and display the roots
# roots = quadratic_roots(a, b, c)
# print("Roots of the quadratic equation:")
# print(f"Root 1: {roots[0]}")
# print(f"Root 2: {roots[1]}")
