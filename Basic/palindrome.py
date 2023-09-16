# Palindrome Number

n = int(input())

a = int(str(n)[::-1])

if n == a:
    print("Palindrome")
else:
    print("Not Palindrome")
    
# Another method

num = int(input())
ans = 0
temp = num

while num > 0:
    mod = num % 10
    ans = ans * 10 + mod
    num = num // 10

if ans == temp:
    print("Palindrome")
else:
    print("Not Palindrome")