#Fibonacci Series
n = int(input("Limit: "))
a = 0
b = 1

for i in range(n):
    print(a, end="\n")
    c = a + b
    a = b
    b = c