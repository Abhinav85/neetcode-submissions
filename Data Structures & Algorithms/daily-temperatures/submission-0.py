class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        res = [0]* len(t)
        stack = []

        for i,t in enumerate(t):
            while stack and stack[-1][1] < t:
                resIndx, resTemp = stack.pop()
                res[resIndx] = (i - resIndx)
            stack.append([i,t])
        
        return res