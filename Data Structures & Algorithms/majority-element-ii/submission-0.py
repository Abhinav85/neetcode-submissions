class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq_map = {}
        for i, num in enumerate(nums):
            if num in freq_map:
                freq_map[num][0] = 1 + freq_map[num][0]
            else:
                freq_map[num] = [1,num]

        ans = []
        
        for count, num in freq_map.values():
            if count > len(nums)//3:
                ans.append(num)
        return ans
