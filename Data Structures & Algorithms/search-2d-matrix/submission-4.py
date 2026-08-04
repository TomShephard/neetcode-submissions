class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom, top = 0, len(matrix) - 1

        while bottom <= top:
            row = (bottom + top) // 2

            if target > matrix[row][-1]:
                bottom = row + 1
            elif target < matrix[row][0]:
                top = row - 1
            else:
                break

        if bottom > top:
            return False
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (r + l) // 2
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        
        return False
        
        

