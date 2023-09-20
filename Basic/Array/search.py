# Search an Element in the Array

arr = []
n = int(input())

for i in range(n):
    i = int(input())
    arr.append(i)

key = int(input())
flag = 0

for i in range(n):
    if arr[i] == key:
        flag = 1
        break

if flag == 1:
    print("Key found")
else:
    print("Key not found")
    
# Another Method
    
    
arr = []
n = int(input())

for i in range(n):
    element = int(input())
    arr.append(element)

key = int(input("Enter the key to search for: "))

if key in arr:
    print("Key found")
else:
    print("Key not found")

    