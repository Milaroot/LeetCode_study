class Solution:
    def minDominoRotations(self, a, b):
        dic = defaultdict(int)
        
        total = a + b
        total_len = 0
        
        poss = []
        
        for i in total:
            dic[i] += 1
            total_len += 1
            
        for i in dic:
            if total_len // 2 <= dic[i]:
                poss.append(i)
        
        ans = int(1e9)
        
        for elem in poss:
            
            curr = 0
            check = 0
            for i in range(len(a)):
                if a[i] != elem:
                    if b[i] == elem: curr += 1
                    else:
                        check = 1
                        break
            if not(check):
                ans = min(ans, curr)
                
            curr = 0
            check = 0
            for i in range(len(b)):
                if b[i] != elem:
                    if a[i] == elem: curr += 1
                    else:
                        check = 1
                        break
            if not(check):
                ans = min(ans, curr)
            
        if ans == int(1e9): return -1
        return ans
            
            
                        
        
            
        
            
        
        