# Prime numbers
num = int(input())
flag = 0


for i in range(2, num):
    if num % i == 0:
        flag = 1
        break
        
if flag == 0:
    print("Prime Number")
else:
    print("Not Prime Number")