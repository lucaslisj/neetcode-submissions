class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0]:
            return False
        if target > matrix[len(matrix) - 1][len(matrix[0]) - 1]:
            return False
        # binary search to find the correct row
        p1 = 0
        p2 = len(matrix) - 1

        best_candidate = -1 # 
        while(p1 <= p2): # find the lowest row such that the leading term is less than the index or equal to it
            mid = p1 + (p2 - p1) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target: #definitely not in this row
                p2 = mid - 1
            else:
                best_candidate = mid # need to include this row cuz the one above it might be
                p1 = mid + 1 
        

      

        row = best_candidate
        i1 = 0
        i2 = len(matrix[0]) - 1
        while (i1 <= i2):
            mid = i1 + (i2-i1) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                i2 = mid - 1
            else:
                i1 = mid + 1
        return False

        