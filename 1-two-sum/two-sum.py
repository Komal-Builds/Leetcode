class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        hashmap = {}
        for i in range(0,n):
            remaning = target - nums[i]
            if remaning in hashmap:
                return [hashmap [remaning],i]
            hashmap[nums[i]] = i    
        