class Solution(object):
    def maxDepth(self, s):
        de=0
        maxi=0
        for ch in s:
            if ch=="(":
                de+=1
                maxi=max(maxi,de)
            elif ch==")":
                de-=1
        return maxi

        