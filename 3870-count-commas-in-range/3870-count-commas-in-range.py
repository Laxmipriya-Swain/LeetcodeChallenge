class Solution(object):
    def countCommas(self, n):
        coma = 0
        for i in range(1,n+1):
            if i >= 1000:
                coma+=1
        return coma

        