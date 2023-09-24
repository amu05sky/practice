# Find Odd or Even Using Bitwise

n= int(input())

if n & 1 == 0:
# uses and operater to check the given i/p is even or odd
    print("Even")
else:
    print("Odd")
    