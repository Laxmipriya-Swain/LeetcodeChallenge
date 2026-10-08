class Solution(object):
    def numIdenticalPairs(self, nums):
        count={}
        ans=0
        for i in nums:
            if i in count:
                ans += count[i]
                count[i] += 1
            else:
                count[i] = 1
        return ans
        