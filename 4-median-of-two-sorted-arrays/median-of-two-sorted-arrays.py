
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:

            p1 = (low + high) // 2
            p2 = (m + n + 1) // 2 - p1

            left1 = float('-inf') if p1 == 0 else nums1[p1 - 1]
            right1 = float('inf') if p1 == m else nums1[p1]

            left2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            right2 = float('inf') if p2 == n else nums2[p2]

            if left1 <= right2 and left2 <= right1:

                if (m + n) % 2 == 1:
                    return max(left1, left2)

                else:
                    return (max(left1, left2) +
                            min(right1, right2)) / 2.0

            elif left1 > right2:
                high = p1 - 1

            else:
                low = p1 + 1

