#Armstrong Number
num = int(input())
a = 0
temp = num

while num > 0:
    mod = num % 10
    a = a + mod * mod * mod
    num = num // 10
    
if a == temp:
    print("Armstrong")
else:
    print("Not Armstrong")