class Solution:
    def climbStairs(self, n):
        one,two = 1,1
        for i in range(n-1):
            temp = two
            two = two + one 
            one = temp
        return two