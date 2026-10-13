class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)
        count={}
        for x in nums:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        result = []
        for x in count:
            if count[x] > n//3:
                result.append(x)
        return result

        