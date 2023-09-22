# Swap Two Numbers Using Bitwise
a = int(input())
b = int(input())

temp = a
a = b
b = temp
print(a,b)

# Another method 
a = int(input())
b = int(input())

a = a ^ b
b = a ^ b
a = a ^ b

print(a, b)