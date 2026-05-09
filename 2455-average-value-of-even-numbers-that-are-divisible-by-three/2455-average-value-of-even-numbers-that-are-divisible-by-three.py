class Solution(object):
    def averageValue(self, nums):
        su = 0
        count = 0
        for i in nums:
            if i % 3 == 0 and i % 2 == 0:
                su += i
                count += 1
        if count == 0:
            return 0
        return su / count
        
        