# Reverse the String - Method 1
str1 = input()
a = str1[::-1]
print(a)

# Reverse the String - Method 2
def legth(self):
    count = 0
    for i in str1:
        count += 1
    return count

str1 = input()
rev_str1 = ""
x = legth(str1)

for i in range(x):
    rev_str1 = str1[i] + rev_str1

print(rev_str1)