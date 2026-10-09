class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        count = 0
        while i <= j:
            curr_sum = people[i] + people[j]
            if curr_sum > limit:
                count = count + 1
                j = j -1
            else:
                i = i + 1
                j = j - 1
                count = count + 1
        return count


        