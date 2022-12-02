class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        res1 = []; res2 = []
        s1 = set(); s2 = set()
        d1 =  defaultdict(int); d2 = defaultdict(int)
        for i in word1: 
            d1[i] += 1
            s1.add(i)
        for i in word2:
            d2[i] += 1
            s2.add(i)
        for i in d1: res1.append(d1[i])
        for i in d2: res2.append(d2[i])
        return (sorted(res1) == sorted(res2)) and (s1 == s2)