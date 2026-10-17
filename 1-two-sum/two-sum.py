class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        premap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in premap:
                return [premap[diff],i]
            premap[n] = i    