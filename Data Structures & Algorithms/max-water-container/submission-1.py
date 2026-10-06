class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area  = 0
        while (l < r):
            curr_area = min(heights[l], heights[r]) * (r - l)
            if heights[r] <= heights[l]:
                r = r -1
            else:
                l = l + 1
            max_area = max(max_area, curr_area)
        return max_area
