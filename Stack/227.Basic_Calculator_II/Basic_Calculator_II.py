class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stk = []
        op = ''
        vis = [0 for i in range(len(s))]
        for i in range(len(s))
            if vis[i] == 0:
                curr_n = ""
                
                if s[i].isdigit():
                    n = i
                    
                    while(n < len(s) and s[n].isdigit()):
                        vis[n] = 1
                        curr_n += s[n]
                        n += 1
                    curr_n = int(curr_n)
                    
                    if op == '-':
                        curr_n *= -1
                        op = ''
                    
                    if op == '*':
                        sp = stk.pop()
                        if sp < 0:
                            curr_n *= -1 * sp
                            curr_n *= -1
                        else: curr_n *= sp
                        op = ''
                    
                    if op == '/':
                        sp = stk.pop()
                        if sp < 0:
                            curr_n = -1 *sp // curr_n
                            curr_n *= -1
                        else: curr_n = sp // curr_n
                        op = ''
                    stk.append(curr_n)
                
                else:
                    if s[i] != '+':
                        op = s[i]
        return sum(stk)
             


        