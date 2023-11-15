# Sum of 2D Array

arr = []
n = int(input())

for i in range(n):
    col = []
    for j in range(n):
        j = int(input())
        col.append(j)
    arr.append(col)
# res=' '.join(map(str, arr))
# print(res)
result = 0

for i in range(n):
    for j in range(n):
        result += arr[i][j]
        
print(result)