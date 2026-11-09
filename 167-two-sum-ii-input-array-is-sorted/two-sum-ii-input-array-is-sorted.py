class Solution(object):
    def twoSum(self, num, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(num) - 1
        while left < right:
            total = num[left] + num[right]
            if total == target:
                return [left + 1, right + 1]
            elif total< target:
                left += 1
            else:
                right -= 1
                            