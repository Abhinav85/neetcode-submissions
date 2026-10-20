class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        res = float('inf')
        curr_sum = 0

        for j in range(len(nums)):
            curr_sum = curr_sum + nums[j]
            while curr_sum >= target:
                curr_sum = curr_sum - nums[i]
                res = min(res, j - i + 1)
                i = i + 1

            
        if res == float('inf'):
            return 0
        return res

        