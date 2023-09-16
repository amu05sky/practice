# sum of digits

num = int(input())
result = 0

while num > 0:
    mod = num % 10
    result = result + mod
    num = num // 10
    
print(result)