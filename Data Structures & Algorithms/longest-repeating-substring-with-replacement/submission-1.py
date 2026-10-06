class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        max_length = 0
        arr = [0]*26

        if len(s) == 0:
            return 0
        

        
        while r < len(s):
            ascii_pos = ord(s[r]) - 65
            arr[ascii_pos] = arr[ascii_pos] + 1
            max_arr = max(arr)
            sum_arr = sum(arr)
            print(arr)
            print(r,l)
            print(sum_arr, max_arr)

            if sum_arr - max_arr <= k:
                max_length = max(max_length, r - l)
            else:
                ascii_pos_l = ord(s[l]) - 65
                arr[ascii_pos_l] = arr[ascii_pos_l] - 1
                l = l + 1
            r = r + 1
        return max_length + 1

        