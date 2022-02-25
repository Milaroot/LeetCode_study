class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {}
        ans = []
        def dfs(s, curr, total):
            
            if len(curr) == total: 
                ans.append(curr)
                return 
            
            for i in dic[s[0]]:
                dfs(s[1:], curr + i, total)
            
        
        dic["2"] = ["a","b","c"]
        dic["3"] = ["d","e","f"]
        dic["4"] = ["g","h","i"]
        dic["5"] = ["j","k","l"]
        dic["6"] = ["m","n","o"]
        dic["7"] = ["p","q","r","s"]
        dic["8"] = ["t","u","v"]
        dic["9"] = ["w","x","y","z"]
        
        if digits =="": return []
        
        dfs(digits, "", len(digits))
        
        return ans
            
        
            
        
        
        
        