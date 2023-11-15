# Sum of the Elements in the Array
arr = []
n = int(input())
s = 0

for i in range(n):
    i = int(input())
    arr.append(i)
for i in range(1,n):
    if i < n:
        s = s + arr[i]
    
print(s)
