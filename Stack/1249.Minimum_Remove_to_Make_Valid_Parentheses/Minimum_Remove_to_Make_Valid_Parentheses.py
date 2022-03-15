class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        arr = list(s)
        
        stk = []
        
        for i, curr in enumerate(s):

            if curr == "(":
                stk.append(i)
                
            if curr == ")":
                if stk != []: stk.pop()
                else: arr[i] = ""
                    
            
                
                    
                    
        for i in stk: arr[i] = ""
        
        return "".join(arr)

#solution 2
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        LeftToRight = []
        l = 0
        for i in s:
            if i == "(":
                l += 1
                LeftToRight.append(i)
            elif i == ")":
                if l > 0:
                    l -= 1
                    LeftToRight.append(i)
            else: LeftToRight.append(i)
                
        RightToLeft = []
        r = 0
        for i in LeftToRight[::-1]:
            if i == ")":
                r += 1
                RightToLeft.append(i)
            elif i == "(":
                if r > 0:
                    r -= 1
                    RightToLeft.append(i)
            else: RightToLeft.append(i)
                
        return "".join(RightToLeft[::-1])




            