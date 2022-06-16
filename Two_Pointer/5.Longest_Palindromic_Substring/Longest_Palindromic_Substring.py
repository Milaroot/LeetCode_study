class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        mx = 1
        curr = 0
        ans = s[0]
        for i in range(1, len(s)):
            l = i - 1; r = i
            curr = 0; curr_l = ""
            while(l > -1 and r < len(s)):
                if s[l] != s[r]:
                    break
                else:
                    curr_l = s[l] + curr_l + s[r]
                    curr += 2
                    if(curr > mx):
                        mx = curr
                        ans = curr_l
                    l -= 1
                    r += 1
        for i in range(1, len(s)):
            l = i - 1; r = i + 1
            curr_l = s[i]
            curr = 1
            while(l > -1 and r < len(s)):
                if s[l] != s[r]:
                    break
                else:
                    curr_l = s[l] + curr_l + s[r]
                    curr += 2
                    if(curr > mx):
                        mx = curr
                        ans = curr_l
                    l -= 1
                    r += 1
        return ans
                    
        
            