# Largest and Smallest Element in the Array

arr = []
n = int(input())

for i in range(n):
    i = int(input())
    arr.append(i)
    
    
a = arr[0]
b = arr[0]

for i in range(n):
    if arr[i] > a:
        a = arr[i]
print("Max = ", a)        
        
for i in range(n):
    if arr[i] < b:
        b = arr[i]
print("Min = ", b)   