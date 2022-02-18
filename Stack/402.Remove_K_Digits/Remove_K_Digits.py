class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for curr in num:
            while(k and stack and stack[-1] > curr):
                stack.pop()
                k -= 1
            stack.append(curr)
        while(k):
            stack.pop()
            k -= 1
        ans = ("".join(stack)).lstrip("0")
        if ans == "": return "0"
        else: return ans
            