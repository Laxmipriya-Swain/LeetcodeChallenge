class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        max_cot=0
        for x in nums:
            if x==1:
                count+=1
                max_cot = max(count,max_cot)
            else:
                count=0
        return max_cot
        