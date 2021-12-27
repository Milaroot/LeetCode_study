class Solution:
    def findComplement(self, num: int) -> int:
        b_num = str(bin(num))[2:]
        ans = 0
        for i in b_num:
            i = 0 if i == '1' else 1   
            ans *= 2
            ans += i
        return ans 

        
        