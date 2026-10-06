class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for n in nums:
            if (n-1) not in numset:
                curr_count = 0
                while (n+curr_count) in numset:
                    curr_count = curr_count + 1
                    longest = max(longest, curr_count)
        return longest
	

        