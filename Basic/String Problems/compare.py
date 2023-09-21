# Compare Two Strings Problem

str1 = input()
str2 = input()

length1 = 0
length2 = 0

for i in str1:
    length1 += 1

for i in str2:
    length2 += 1
    

if length1 == length2:
    print("Yes")
else:
    print("No")
    
# Another Method

str1 = input()
str2 = input()

length1 = 0
length2 = 0

for i in str1:
    length1 += 1

for i in str2:
    length2 += 1

status = 0

if length1 == length2:
    for i in range(length1):
        if str1[i] != str2[i]:
            status += 1
            print("No")
            break
    else:
        print("Yes")
            
else:
    print("No")