class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0    #boyer moore majority vote algorithum
        count = 0
        for n in nums :
            if count == 0:
                res = n
            count += (1 if n == res else -1) 
        return res       

            

        