# Count Odd and Even Elements
arr = []
size = int(input())


for i in range(size):
    i = int(input())
    arr.append(i)
    
odd_count = 0
even_count = 0

for i in range(size):
    if arr[i] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
   
print("Even Number Count = ", even_count,"Odd Number Count = ", odd_count)