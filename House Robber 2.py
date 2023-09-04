class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        rob1, rob2 = 0,0
        for i in range(0,len(nums)-1):
            temp = max(nums[i] + rob1,rob2)
            rob1 = rob2
            rob2 = temp
        sub1 = rob2
        rob1, rob2 = 0,0
        for i in range(1,len(nums)):
            temp = max(nums[i] + rob1,rob2)
            rob1 = rob2
            rob2 = temp
        return max(sub1,rob2)
