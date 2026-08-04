class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo, hi = 0, len(matrix) - 1

        while lo <= hi:
            midrow = (hi + lo) // 2

            if matrix[midrow][-1] < target:
                lo = midrow + 1
            elif matrix[midrow][0] > target:
                hi = midrow - 1
            else:
                break
        
        

        l, r = 0, len(matrix[midrow]) - 1

        while l <= r:
            mid = (r + l) // 2
            if matrix[midrow][mid] < target:
                l = mid + 1
            elif matrix[midrow][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False


