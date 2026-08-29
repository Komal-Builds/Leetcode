class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}
        for word in strs:
            count = [0]*26
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key not in groups:
                groups[key] = []

            groups[key].append(word)
        return list(groups.values())        
        