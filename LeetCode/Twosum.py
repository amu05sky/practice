#1. Two Sum
#Two ways 
#1.Double forloop (Brute force)- 0(n^2): as it is a nested loop 
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # go through everything expect last digit
        for i in range(len(nums)-1):
            #will start from current index go to end of nums
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return([i,j])
                
# nums= [1,9,6,7,123,6]
# target= int(input())
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i,j)
# print()

#2.Dictionary storage.0(n)
# leet code solution 
class Sol:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen ={}
        for i, num in enumerate(nums):
            if target - num in seen:
                return([seen[target - num], i])
            elif num not in seen:
                seen[num]= i
        

# a= [123,456,78,34,1,2,3,4,5,6,7]
# target=int(input())
# d={}
# for i,val in enumerate(a):
#     x= target-a[i]
#     if x in d:
#         print(d[x],i)
#     d[val] =i
# print()
        