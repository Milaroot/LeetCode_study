class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        mp = defaultdict(list); ans = 0
        for word in words: mp[word[0]].append(word)
        for word in s:
            tmp = copy.copy(mp[word])
            mp[word].clear()
            for curr_elemt in tmp:
                if len(curr_elemt) == 1: ans += 1
                else: mp[curr_elemt[1]].append(curr_elemt[1:])
        return ans
            
            