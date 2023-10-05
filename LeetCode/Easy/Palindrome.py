# 9. Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a=0
        temp=x
        while temp>0:
            mod=temp%10
            a=a*10+mod
            temp=temp//10
        if x==a:
            return True
        else:
            return False