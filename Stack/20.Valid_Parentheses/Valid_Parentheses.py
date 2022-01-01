class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        obj = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for i in range(len(s)):
            el = s[i]
        
            if el in ['[','{','(']:
                stack.append(el)
            elif len(stack) and stack[-1]  == obj[el] :
                stack.pop()
            else:
                stack.append(el)
        return not bool(len(stack))