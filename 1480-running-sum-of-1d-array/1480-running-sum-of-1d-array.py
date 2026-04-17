class Solution(object):
    def runningSum(self, nums):
        st=[]
        re=0
        for i in nums:
            re+=i
            st.append(re)
        return st 

        
        