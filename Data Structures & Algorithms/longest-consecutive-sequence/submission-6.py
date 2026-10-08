class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set()
        for num in nums:
            exists.add(num)
        
        if len(nums) <= 1:
            return len(nums)
        
        ans = 1
        for num in nums:
            temp = 1
            to_check = num
            if num - 1 not in exists:
                while temp > 0:
                    if to_check + 1 in exists:
                        temp = temp + 1
                        ans = max(temp, ans)
                        to_check = to_check + 1
                    else:
                        temp = 0

        return ans


        