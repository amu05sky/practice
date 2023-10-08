# 13. Roman to Integer

s=input()
m = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
ans = 0
        
for i in range(len(s)):
    if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
        ans -= m[s[i]]
    else:
        ans += m[s[i]]
print(ans)

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         m = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000
#         }
        
#         ans = 0
        
#         for i in range(len(s)):
#             if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
#                 ans -= m[s[i]]
#             else:
#                 ans += m[s[i]]
        
#         return ans

# def roman_to_integer(s):
#     roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     result = 0
#     prev_value = 0
    
#     for i in reversed(s):
#         current_value = roman_dict[i]
#         if current_value < prev_value:
#             result -= current_value
#         else:
#             result += current_value
#         prev_value = current_value
    
#     return result

# # Example usage:
# roman_numeral = "MCMXCIV"  # This represents 1994 in Roman numerals
# integer_value = roman_to_integer(roman_numeral)
# print(integer_value)  # Output will be 1994