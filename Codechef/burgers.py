c= int(input())


for i in range(c):
    a, b = map(int, input().split())
    if a==b or a<b:
        print(a)
    else:
        print(b)
