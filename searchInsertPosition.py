def searchInsert(nums,target):
    left=0
    right=len(nums)-1
    while left<right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            left=left+1
        else:
            right=right-1
    return left
nums = [1,3,5,6]
target = 5
output=searchInsert(nums,target)
print(output)
    