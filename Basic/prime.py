# Prime numbers
num = int(input())
flag = 0 # boolean value to check prime number
# we take flag and assume the number to be prime
# and check the credibility
for i in range(2, num):
    if num % i == 0:
        flag = 1
        break
        
if flag == 0:
    print("Prime Number")
else:
    print("Not Prime Number")