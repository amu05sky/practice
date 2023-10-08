# 412. Fizz Buzz
n=int(input())
x=[]
for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
        i = "FizzBuzz"
    elif i%3 == 0:
        i = "Fizz"
    elif i%5 ==0:
        i = "Buzz"
    else:
        i = str(i)
    x.append(i)
print(str(x))
# LeetCode Solution
# class Solution:
    # def fizzBuzz(self, n: int) -> List[str]:
    #     x=[]
    #     for i in range(1,n+1):
    #         if i%3 == 0 and i%5 == 0:
    #             i = "FizzBuzz"
    #         elif i%3 == 0:
    #             i = "Fizz"
    #         elif i%5 ==0:
    #             i = "Buzz"
    #         else:
    #             i = str(i)
    #         x.append(i)
    #     return x