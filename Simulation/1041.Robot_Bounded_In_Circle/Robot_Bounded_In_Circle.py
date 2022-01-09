class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        arr = [[0,1], [-1, 0], [0, -1], [1, 0]]; curr = [0, 0]
        dire = 0
        for i in instructions:
            if i == 'G':
                curr[0] += arr[dire][0]
                curr[1] += arr[dire][1]
            elif i == 'L': 
                dire += 1
                dire %= 4
            elif i == 'R': 
                dire -= 1
                dire %= 4 
        return True if curr == [0, 0] or dire != 0 else False
        