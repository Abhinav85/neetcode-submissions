class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        num_set = set()
        for num in nums:
            num_set.add(num)
        ans = 1
        
        for num in nums:
            if num-1 not in num_set:
                res = 1
                target = num + 1
                while target in num_set:
                    res = res + 1
                    ans = max(res,ans)
                    target = target + 1
        return ans


        