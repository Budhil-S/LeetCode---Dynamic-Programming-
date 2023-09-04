class Solution:
    def maxProduct(self, nums) -> int:
        result = max(nums)
        max_sub, min_sub = 1,1
        for num in nums:
            temp = num * max_sub
            max_sub = max(num * max_sub,num * min_sub,num)
            min_sub = min(temp,num * min_sub,num)
            result = max(result,max_sub)
        return result
            