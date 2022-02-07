class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        curr = 0
        for i in s: curr ^= ord(i)
        for j in t: curr ^= ord(j)
        return chr(curr) 
            