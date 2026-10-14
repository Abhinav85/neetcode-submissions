class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]
        count = 0

        while l <= r:
            if left_max > right_max:
                right_max = max(height[r], right_max)
                count = count + right_max - height[r]
                r = r -1
            else:
                left_max = max(height[l], left_max)
                count = count + left_max - height[l]
                l = l + 1
        return count