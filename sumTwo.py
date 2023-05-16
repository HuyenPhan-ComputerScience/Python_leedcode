class Solution(object):
   # def sumtwo(selfs,nums,target):
   #     require={}
   #     for i in range (len(nums)):
   #         if target-nums[i] in require:
   #             return {require[target-nums[i]],i}
   #         else: require[nums[i]]=i
   def sumtwo(selfs,nums,target):
       require={};
       for i in range (len(nums)):
           if target-nums[i] in require:
               return {i,require[target-nums[i]]}
           else:
               require[nums[i]]=i

num=[1,2,3,5,6]
ob1=Solution()
print(ob1.sumtwo(num,5))
