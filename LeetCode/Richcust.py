# 1672. Richest Customer Wealth
accounts = [[2,3],[3,4],[4,5]]
Max=0
for i in accounts:
    Sum=0
    for k in i:
        Sum=Sum + k
        if Max < Sum:
            Max = Sum
    
print(Max)# o/p: 9

#for  O/p: 5,7,9
# accounts = [[2,3],[3,4],[4,5]]
# Max=0
# for i in accounts:
#     Sum=0
#     for k in i:
#         Sum=Sum + k
#         if Max < Sum:
#             Max = Sum
    
# print(Max)

#Another method
# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         return max([sum(acc) for acc in accounts])