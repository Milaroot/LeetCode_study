class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(int)
        for i, c in enumerate(s): dic[c] = i
            
        ans = []
        arr = list(map(dic.__getitem__, s))
        
        i = target = curr = 0
        
        while(i != len(arr)):
            target = max(arr[i], target)
            curr +=1
            if i == target:
                ans.append(curr)
                curr = 0
            i += 1
                
        return ans
            
            
        