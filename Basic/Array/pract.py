# nested list sum
arr = []
n = int(input())
x = int(input())
for i in range(n):
    col = []
    for j in range(x):
        j = int(input())
        col.append(j)
    arr.append(col)
    
for i in range(1,n):
     for j in range(1,x):
         s= col[0]
         s +=col[j]
print(s)

# Sum of total list 
arr= [7,1,3]
s= arr[0]
for i in range(1,len(arr)):
    s +=arr[i]
print(s)
    