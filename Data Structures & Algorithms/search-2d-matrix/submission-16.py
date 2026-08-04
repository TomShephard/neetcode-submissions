class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        if l > r:
            return False

        while l <= r:
            m = (r+l) // 2

            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break
        
        l, r = 0, len(matrix[m]) - 1
        while l <= r:
            mid = (l + r) // 2

            if target > matrix[m][mid]:
                l = mid + 1
            elif target < matrix[m][mid]:
                r = mid - 1
            else:
                return True
        
        return False
