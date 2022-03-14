class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stk = []
        for i in arr:
            if i == "":
                continue
            elif i == '..':
                if stk != []: stk.pop()
            elif i != ".":
                stk.append(i)
        
        if stk == []: return "/"
        else: return "/" + ("/".join(stk))
    
    """ppyy solution
    class Solution:
        def simplifyPath(self, path: str) -> str:
            return os.path.normpath(path)
    """