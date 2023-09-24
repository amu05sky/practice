# Check Nth Bit is Set or Unset

num = int(input())
n = int(input())

num = num & (1 << n-1)

if num == 0:
    print("OFF")
else:
    print("ON")