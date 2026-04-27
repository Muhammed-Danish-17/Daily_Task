class Solution(object):
    def fizzBuzz(self, n):
        strr = []
        for i in range(1,n + 1):
            if i % 3 == 0 and i % 5 == 0:
                strr.append("FizzBuzz")
            elif i % 3 == 0:
                strr.append("Fizz")
            elif i % 5 == 0:
                strr.append("Buzz")
            else:
                strr.append(str(i))
        return strr