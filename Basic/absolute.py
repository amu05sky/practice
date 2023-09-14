num = int(input("Enter:"))

if num < 0:
    print(-1*num)
else:
    print(num)
    
    
# Another method
num = int(input("Enter:"))
if num < 0:
    num = -num
    
print(num)