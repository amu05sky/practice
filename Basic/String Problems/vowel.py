# Count Vowels in a String

str1 = input()
length = 0

for i in str1:
    if i =="a" or i=='e' or i=='i' or i =="o" or i=='u' or i=='A' or i=='E' or i=='I' or i =="O" or i=='U':
        length += 1
print(length)