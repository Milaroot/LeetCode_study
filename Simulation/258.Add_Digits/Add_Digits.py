class Solution:
    def addDigits(self, num: int) -> int:
        while(num >= 10):
            curr = 0
            num = str(num)
            for i in num: curr += int(i)
            num = curr
        return num