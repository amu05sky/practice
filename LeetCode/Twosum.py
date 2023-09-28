#Two ways 
#1.Double forloop (Brute force)- 0(n^2)
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # go through everything expect last digit
        for i in range(len(nums)-1):
            #will start from current index go to end of nums
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return([i,j])
                


#2.Dictionary storage.0(n)
class Sol:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen ={}
        for i, num in enumerate(nums):
            if target - num in seen:
                return([seen[target - num], i])
            elif num not in seen:
                seen[num]= i
        
        
        
# leet code solution 
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         seen ={}
#         for i, num in enumerate(nums):
#             if target - num in seen:
#                 return([seen[target - num], i])
#             elif num not in seen:
#                 seen[num]= i
    