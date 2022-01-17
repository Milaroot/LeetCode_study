class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()
        if len(pattern) != len(s): return False

        hash_map = {}
        rep = []

        for i in range(len(pattern)):
            if pattern[i] not in hash_map:
                if s[i] in rep: return False
                hash_map[pattern[i]] = s[i]
                rep.append(s[i])
            else: 
                if hash_map[pattern[i]] != s[i]: return False
                else: continue
        return True