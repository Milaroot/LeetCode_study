class Solution:
    def pushDominoes(self, dominoes: str) -> str:
            dominoes = "L" + dominoes + "R"
            l, ans = 0, ""
            for r in range(1, len(dominoes)):
                if dominoes[r] == ".": continue
                if l != 0: ans += dominoes[l]
                mid = r - l - 1
                if dominoes[r] == dominoes[l]: 
                    for _ in range(mid): ans += dominoes[l]
                elif dominoes[r] == "R" and dominoes[l] == "L":
                    for _ in range(mid): ans += "."
                else: 
                    ans += 'R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2)
                l = r
            return ans