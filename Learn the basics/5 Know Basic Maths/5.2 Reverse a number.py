class Solution:
    def reverseNumber(self, n):
        rev_int = 0
        while(n):
            last_digi = n % 10
            n = n//10
            rev_int = rev_int*10 + last_digi
        return rev_int