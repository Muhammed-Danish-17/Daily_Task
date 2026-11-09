class Solution(object):
    def numberOfSteps(self, num):
        num2=0
        while num>0:
            if num %2==0:
                num=num/2
                num2=num2+1
            else:
                num=num-1
                num2=num2+1
        return num2
