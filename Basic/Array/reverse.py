# Reverse the Array

arr = []
n = int(input())

for i in range(n):
    i = int(input())
    arr.append(i)

lastIndex = n-1

for i in range(n//2):
    temp = arr[i]
    arr[i] = arr[lastIndex-i]
    arr[lastIndex-i] = temp

for i in range(n):
    print(arr[i], end=" ")


# Another Method
arr = []
n = int(input())

for i in range(n):
    i = int(input())
    arr.append(i)

reversed_array = arr[::-1]
print(reversed_array)