class Solution:
    def isPathCrossing(self, path: str) -> bool:
        mp = defaultdict(int)
        
        mp[(0,0)] += 1
        
        curr = [0,0]
        
        for i in path:
            if i == "N": curr[1] += 1
            if i == "S": curr[1] += -1
            if i == "W": curr[0] += -1
            if i == "E": curr[0] += 1
            
            tmp = tuple(curr)
            
            if mp[tmp] != 0: return True
            else: mp[tmp] = 1
        
        
        return False
        