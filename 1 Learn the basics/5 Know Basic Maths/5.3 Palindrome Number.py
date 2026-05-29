class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        
        copy = x 
        rev_num = 0

        while copy:
            last_digit = copy % 10
            copy = copy // 10
            rev_num = rev_num * 10 + last_digit
        
        if rev_num == x: 
            return True
        else:
            return False