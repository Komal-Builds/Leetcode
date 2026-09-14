class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count = [0] * 20001

        for num in nums:
            count[num + 10000] += 1

        for i in range(20000, -1, -1):
            if count[i] > 0:
                k -= count[i]

                if k <= 0:
                    return i - 10000