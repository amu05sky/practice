# Largest Element in the Array

arr = []
n = int(input())

for i in range(n):
    i = int(input())
    arr.append(i)
    
m = arr[0]

for i in range(n):
    if arr[i] > m:
        m = arr[i]
        
print("Max = ",m)
       