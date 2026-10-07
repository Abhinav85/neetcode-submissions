class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, l ,r):
            m = (l + r) // 2
            left_sub_arr, right_sub_arr = arr[l: m+1], arr[m+1: r + 1]
            i, j, k = 0,0,l

            while i < len(left_sub_arr) and j < len(right_sub_arr):
                if left_sub_arr[i] >= right_sub_arr[j]:
                    arr[k] = right_sub_arr[j]
                    j = j + 1
                    k = k + 1
                else:
                    arr[k] = left_sub_arr[i]
                    i = i +1
                    k = k +1
            
            while i < len(left_sub_arr):
                arr[k] = left_sub_arr[i]
                k = k +1
                i = i +1

            while j < len(right_sub_arr):
                arr[k] = right_sub_arr[j]
                k = k +1
                j = j +1

        def mergeSort(arr,l,r):
            if l == r:
                return arr
            m = (l + r) // 2
            mergeSort(arr,l,m)
            mergeSort(arr,m+1,r)
            merge(arr,l,r)

        mergeSort(nums,0,len(nums)-1)
        return nums

        
