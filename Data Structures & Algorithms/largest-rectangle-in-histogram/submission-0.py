class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area_arr = []
        max_area = 0

        for pos, num in enumerate(heights):
            print (max_area)
            start = pos

            while stack and stack[-1][0] > num:
                last_num,last_pos = stack.pop()
                max_area = max(last_num * (pos - last_pos), max_area)
                start = last_pos
            stack.append([num, start])
                
        for num1, pos1 in stack:
            max_area = max(num1 * (len(heights) - pos1), max_area)
        
        return max_area
        