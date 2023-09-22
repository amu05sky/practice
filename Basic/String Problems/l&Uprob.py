# Lower and Upper Problem

str1 = input()
print(str1.swapcase())

# Another method

str1 = input()
length = 0
newstr = ""

for i in str1:
    length += 1

for i in range(length):
    if (str1[i] >= 'a') and (str1[i] <= 'z'):
        newstr = newstr + chr(ord(str1[i]) - 32)
    elif (str1[i] >= 'A') and (str1[i] <= 'Z'):
        newstr = newstr + chr(ord(str1[i]) + 32)

print(newstr)