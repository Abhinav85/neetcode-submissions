class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        product, product_without_zero = 1, 1
        zero_count = 0
        for n in arr:
            product = product * n
            if n!= 0:
                product_without_zero = product_without_zero*n
            if n == 0:
                zero_count = zero_count + 1
        
        return_arr = []
        for n in arr:
            if zero_count > 1:
                return_arr.append(0)
            elif n == 0:
                return_arr.append(product_without_zero)
            else:
                return_arr.append(int(product/n))
        return return_arr

        
        