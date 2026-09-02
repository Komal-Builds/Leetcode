class Solution(object):
    def maxProduct(self, nums):
        curmax = nums[0]
        curmin = nums[0]
        res = nums[0]

        for n in nums[1:]:
            old_max = curmax
            old_min = curmin

            curmax = max(n, n * old_max, n * old_min)
            curmin = min(n, n * old_max, n * old_min)

            res = max(res, curmax)

        return res