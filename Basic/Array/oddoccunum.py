arr = []
size = int(input())

for i in range(size):
    i = int(input())
    arr.append(i)

result =  arr[0]   
for i in range(1, size):
    result = result ^ arr[i]
print(result)
    