class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        k = 0
        ans = set()
        while k < len(nums) - 2:
            l = k + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r] + nums[k]
                if curr_sum > 0:
                    r = r -1
                elif curr_sum < 0:
                    l = l + 1
                else:
                    ans.add((nums[l], nums[r], nums[k]))
                    l = l + 1
                    r = r - 1
            k = k + 1

        return list(ans)
        