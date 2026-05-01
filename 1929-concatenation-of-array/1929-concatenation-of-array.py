class Solution(object):
    def getConcatenation(self, nums):
        dup=[]
        for i in nums:
            dup.append(i)
        for i in nums:
            dup.append(i)
        return dup
        