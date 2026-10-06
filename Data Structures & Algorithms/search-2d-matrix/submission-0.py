class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l_out = 0
        r_out = len(matrix) - 1
        binary_search_index = 0

        while l_out <= r_out:
            mid_out = (l_out + r_out) // 2
            if matrix[mid_out][0] > target:
                r_out = mid_out - 1
            elif matrix[mid_out][-1] < target:
                l_out = mid_out + 1
            else:
                break

        if l_out > r_out:
            return False
            
        binary_search_index = (l_out + r_out)//2



        search_arr = matrix[binary_search_index]
        l = 0
        r = len(search_arr) - 1
        
        while l <= r:
            mid = int((l + r)/2)
            print(mid, search_arr[mid])
            if search_arr[mid] < target:
                l = mid + 1
            elif search_arr[mid] > target:
                r = mid - 1
            else:
                return True
            print(r,l)
        return False

        