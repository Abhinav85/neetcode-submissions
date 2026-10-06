class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles):
            return -1
        max_eating_speed = max(piles)
        min_eating_speed = 1
        res = max_eating_speed
        
        while min_eating_speed <= max_eating_speed:
            trial = (min_eating_speed + max_eating_speed) // 2
            eating_time = 0
            for i in piles:
                eating_time = eating_time + math.ceil(float(i)/trial)
            if eating_time <= h:
                res = trial
                max_eating_speed = trial - 1
            else :
                min_eating_speed = trial + 1
        return res
            