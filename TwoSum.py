class Solution(object):
    def twoSum(self, nums, target):
        
        twoSumMap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in twoSumMap:
                return twoSumMap[complement], i

            twoSumMap[nums[i]] = i
        
        return []