class Solution(object):
    def reverse(self, x):
        n=abs(x)
        revnum=0
        while n > 0:
            lastdigit = n%10
            revnum=revnum *10 + lastdigit
            n = n//10
        #for -ve checking
        if x<0:
            revnum = -revnum
        if -2**31 <= revnum <= 2**31-1:
            return revnum
        return 0
        
        
        