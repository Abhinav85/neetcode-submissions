class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq_map = set()
        l = 0
        for r in range(len(nums)):
            if r - l > k:
                freq_map.remove(nums[l])
                l =  l+ 1
            if nums[r] in freq_map:
                return True
            freq_map.add(nums[r])
        return False                


        
        