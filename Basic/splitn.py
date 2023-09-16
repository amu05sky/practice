# Spliting of numbers into digit
num = int(input())

while num > 0:
    mod = num % 10
    print(mod)
    num = num // 10
    
