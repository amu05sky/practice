# 1480. Running Sum of 1d Array
arr =[]
size = int(input())
for i in range(size):
    arr.append(int(input()))
for i in range(1,len(arr)):
    arr[i] += arr[i-1]

print(arr)

#Leet code solution
# class Solution:
#     def runningSum(self, arr: List[int]) -> List[int]:
#         for i in range(1,len(arr)):
#             arr[i] += arr[i-1]
#         return arr