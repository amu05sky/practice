# Palindrome of the String

x = input()

a = x[::-1]

if x == a:
    print("Palindrome")
else:
    print("Not Palindrome")
    
# Another method

def length(str1):
    count = 0
    for i in str1:
        count += 1
    return count

str1 = input()
reverse_str1 = ""
len1 = length(str1)
lastIndex = len1 - 1

for i in range(len1//2):
    if str1[i] != str1[lastIndex-i]:
        print("Not Palindrome")
        break
else:
    print("Palindrome")
