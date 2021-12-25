class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        b = bin(n)[2:]
        if b.count('1') == 1: return True
        return False