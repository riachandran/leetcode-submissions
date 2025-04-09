class Solution:
    def reverse(self, x: int) -> int:
        sign,i,res = 1,0,0
        if x < 0: 
            sign = -1
            x *= -1
        if x == 0: return x
        while x > 0:
            rem = x % 10
            res = res*10 + rem
            x //= 10

        if sign*res < -2**31 or sign*res > 2**31 - 1: return 0
        
        return sign*res
