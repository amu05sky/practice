# Print the Given Pattern

n = int(input())

for i in range(n):
    for j in range(n):
        if i <= n and j <= i:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
# Print the Given Pattern 2

n = int(input())

for i in range(n):
    for j in range(i+1):
            print("*",end="")

    print()