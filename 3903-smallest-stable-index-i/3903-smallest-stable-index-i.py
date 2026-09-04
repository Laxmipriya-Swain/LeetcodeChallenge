class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # Minimum from i to the end
        right_min = [0] * n
        right_min[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            right_min[i] = min(nums[i], right_min[i + 1])

        # Maximum from 0 to i
        max_left = nums[0]

        for i in range(n):
            max_left = max(max_left, nums[i])

            if max_left - right_min[i] <= k:
                return i

        return -1