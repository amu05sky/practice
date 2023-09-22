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

while temp > 0:
    mod = temp % 10
    ans = ans * 10 + mod
    temp = temp // 10

if ans == num:
    print("Palindrome")
else:
    print("Not Palindrome")