class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum=n*(n+1)//2
        act_sum=sum(nums)
        return expected_sum - act_sum

        