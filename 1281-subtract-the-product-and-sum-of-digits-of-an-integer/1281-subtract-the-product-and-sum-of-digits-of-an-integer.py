class Solution(object):
    def subtractProductAndSum(self, n):
        degits=str(n)
        product=1
        total=0
        for d in degits:
            digits=int(d)
            product*=digits
            total+=digits
        return product-total
       