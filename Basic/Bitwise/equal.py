# Find Equal or Not Using Bitwise

num1 = int(input())
num2 = int(input())

if num1 == num2:
    print("Equal")
else:
    print("Unequal")
    
# Another Method 
num1 = int(input())
num2 = int(input())

if num1 ^ num2 == 0:
    print("Equal")
else:
    print("Unequal")