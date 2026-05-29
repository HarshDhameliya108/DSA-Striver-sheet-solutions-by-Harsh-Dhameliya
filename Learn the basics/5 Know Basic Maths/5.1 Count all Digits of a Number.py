class Solution:
    def countDigit(self, n):
        count = 0
        while(n):
            n = int(n/10)
            count += 1
        return count