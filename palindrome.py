class Solution(object):
    def isPalindrome(selfs,x:int)->bool:
        if x<0:
            return False
        div=1
        while x>=10*div:
            div=div*10
        while x:
            right=x%10
            left=x//div
            if left!=right:return False
            x=(x%div)//10
            div=div/100
            return True
x=1221
ob1=Solution()
print(ob1.isPalindrome(x))
