class Solution:
    def longestSubarray(self, nums, k):

        n = len(nums)
        M = max(nums)

        # Smallest Prime Factor
        spf = list(range(M + 1))

        for i in range(2, int(M ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, M + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        # Prime factors of every number
        factors = [[] for _ in range(M + 1)]

        for x in range(2, M + 1):
            if spf[x] == x:       # x is prime
                for j in range(x, M + 1, x):
                    factors[j].append(x)

        # Sliding window
        freq = [0] * (M + 1)

        left = 0
        distinct = 0
        ans = 0

        for right in range(n):

            for p in factors[nums[right]]:
                if freq[p] == 0:
                    distinct += 1
                freq[p] += 1

            while distinct > k:

                for p in factors[nums[left]]:
                    freq[p] -= 1

                    if freq[p] == 0:
                        distinct -= 1

                left += 1

            ans = max(ans, right - left + 1)

        return ans