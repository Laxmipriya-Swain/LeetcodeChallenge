class Solution(object):
    def countSpecialIntegers(self, nums):
        position = {}
        for i, v in enumerate(nums):
            if v not in position:
                position[v] = []
            position[v].append(i)
        count = 0
        for id in position.values():
            if len(id) < 3:
                continue
            gap = []
            for j in range(len(id) - 1):
                gap.append(id[j + 1] - id[j])
            if len(set(gap)) == 1:
                count += 1
        return count
        