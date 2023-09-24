# Disable Nth Bit of a Number

num = int(input())
n = int(input())

num = num & ~(1 << n-1)

print(num)