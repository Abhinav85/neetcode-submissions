class Solution:
    def trap(self, arr: List[int]) -> int:
        r = len(arr) - 1
        l = 0
        trapped = 0
        leftMax = arr[l]
        rightMax = arr[r]

        while l < r:
            if (rightMax > leftMax):
                l = l + 1
                leftMax = max(leftMax, arr[l])
                trapped = trapped + leftMax - arr[l]

            else:
                r = r - 1
                rightMax = max(arr[r], rightMax)
                trapped = trapped + rightMax - arr[r]

        return trapped

        