class Solution(object):
    def countSpecialIntegers(self, nums):
        count=0
        for x in set(nums):
            id = []
            for i,v in enumerate(nums):
                if v==x:
                    id.append(i)
            if len(id)==3 and id[2]-id[1] == id[1]-id[0]:
                count+=1
        return count