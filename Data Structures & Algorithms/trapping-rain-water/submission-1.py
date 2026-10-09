class Solution:
    def trap(self, height: List[int]) -> int:
        l  = 0
        r  = len(height) - 1

        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l = l +1
                leftMax = max(height[l], leftMax)
                res = res + (leftMax - height[l])
            else:
                r = r - 1
                rightMax = max(height[r], rightMax)
                res = res + (rightMax - height[r])
        return res

        