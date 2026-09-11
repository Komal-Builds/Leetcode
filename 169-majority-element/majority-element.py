class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        element = None
        for num in nums:
            if count == 0:
                element = num
            if num == element:
                count += 1
            else:
                count -= 1
        return element            
            
    

            

        