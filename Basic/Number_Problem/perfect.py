# Perfect Number

import math

n = int(input())
result = 1
a = int(math.sqrt(n))

for i in range(2, a + 1):
    if n % i == 0:
        if n // i == i:
            result = result + i
        else:
            result = result + i + n / i
            
if (result == n):
    print("Yes")
else:
    print("No")