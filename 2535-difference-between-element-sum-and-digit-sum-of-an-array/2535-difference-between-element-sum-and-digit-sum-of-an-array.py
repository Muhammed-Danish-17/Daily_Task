class Solution(object):
    def differenceOfSum(self, nums):
        first=sum(nums)
        second=0
        for num in nums:
            for i in str(num):
                second+=int(i)
        return first-second
        
        