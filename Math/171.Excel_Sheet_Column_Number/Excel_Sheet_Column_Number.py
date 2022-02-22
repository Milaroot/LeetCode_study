class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for i in columnTitle:
            total *= 26
            total += ord(i) - 64
        return total