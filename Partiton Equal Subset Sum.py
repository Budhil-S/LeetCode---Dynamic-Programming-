class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums) / 2
        for i in range(len(nums) -1,-1,-1):
            nextDP = set()
            for tar in dp:
                if(tar + nums[i] == target):
                    return True
                nextDP.add(tar+nums[i])
                nextDP.add(tar)
            dp = nextDP
        if target in dp:
            return True
        else:
            return False