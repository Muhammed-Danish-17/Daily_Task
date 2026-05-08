class Solution(object):
    def returnToBoundaryCount(self, nums):
        arr = 0
        count=0

        for i in nums:
            arr += i
            if arr == 0:
                count+=1
        return count