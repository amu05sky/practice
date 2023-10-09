# 1342. Number of Steps to Reduce a Number to Zero
num=int(input())
steps = 0
    
while num > 0:
    if num % 2 == 0:
        num = num // 2
    else:
        num -= 1
    steps += 1
    
print(steps)



#LeetCode Solution
# class Solution:
#     def numberOfSteps(self, num: int) -> int:
#         steps = 0
#         while num > 0:
#             if num % 2 == 0:
#                 num = num // 2
#             else:
#                 num -= 1
#             steps += 1
#         return steps