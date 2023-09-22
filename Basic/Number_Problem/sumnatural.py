#Sum of Natural  Numbers
#first method
N = int(input())
sum = 0

for i in range(N+1):
    sum += i

print(sum)


#second method
n = int(input())

sum = (n*(n+1)/2)

print(int(sum))