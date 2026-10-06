class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        final_arr = [1] * len(arr)

        for i in range(1, len(arr)):
            final_arr[i] = final_arr[i - 1] * arr[i - 1]

        product_from_right = 1
        for i in range(len(arr) - 1, -1, -1):
            final_arr[i] *= product_from_right
            product_from_right *= arr[i]

        return final_arr

        
        