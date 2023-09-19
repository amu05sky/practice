# Print Diagonals of a N X N Box

num = int(input())

for i in range(num):
    for j in range(num):
        if i == j or i + j == num - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()