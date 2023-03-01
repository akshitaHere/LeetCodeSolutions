class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Divide and conquer : Merge sort
        #Time : O(n log n), Space : O(n)
        #Merge Sort space complexity will always be O(n) including with arrays. If you draw the space tree out, it will seem as though the space complexity is O(nlgn). However, as the code is a Depth First code, you will always only be expanding along one branch of the tree, therefore, the total space usage required will always be bounded by O(3n) = O(n).
        
        def merge(arr, l, r, m):
            left, right = arr[l:m + 1], arr[m + 1: r + 1]
            i, l1, l2 = l, 0, 0

            while l1 < len(left) and l2 < len(right):
                if left[l1] <= right[l2]:
                    arr[i] = left[l1]
                    l1 += 1
                    i += 1
                else:
                    arr[i] = right[l2]
                    l2 += 1
                    i += 1

            while l1 < len(left):
                arr[i] = left[l1]
                l1 += 1
                i += 1

            while l2 < len(right):
                arr[i] = right[l2]
                l2 += 1
                i += 1

            return arr

        def mergeSort(arr, l, r):
            if l == r:
                return arr
            mid = (l + r) // 2
            mergeSort(arr, l, mid)
            mergeSort(arr, mid + 1, r)

            merge(arr, l, r, mid)
            return arr
        
        return mergeSort(nums, 0, len(nums) - 1)