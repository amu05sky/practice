# Concatenate Two Strings
str1 = input()
str2 = input()
str3 = ''

str3 = str1 + str2
print(str3)

# Another Method
str1 = input()
str2 = input()
str3 = ''

for i in str1:
    str3 += i

for i in str2:
    str3 += i

print(str3)