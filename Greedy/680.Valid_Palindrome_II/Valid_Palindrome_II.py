class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0; r = len(s) - 1
        flag = 1
        while(l <= r):
            if s[l] != s[r]:
                flag = 0
                curr_mid = s[l + 1: r]
                if (s[l] + curr_mid)[::-1] == (s[l] + curr_mid): flag = 1
                if (curr_mid + s[r])[::-1] == (curr_mid + s[r]): flag = 1
                break
            else:
                l += 1
                r -= 1
                
        return flag == 1
        