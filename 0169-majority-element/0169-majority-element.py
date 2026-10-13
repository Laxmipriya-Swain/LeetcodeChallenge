class Solution(object):
    def majorityElement(self, nums):
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        n = len(nums)
        for i in count:
            if count[i] > n//2:
                return i


        