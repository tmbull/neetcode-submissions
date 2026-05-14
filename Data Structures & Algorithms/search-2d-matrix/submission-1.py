class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        start = 0
        end = num_rows
        # find the row first, then the column
        if target < matrix[0][0] or \
            target > matrix[num_rows - 1][num_cols - 1]:
            return False

        while start < end:
            row = start + ((end - start) // 2)
            if target >= matrix[row][0] and target <= matrix[row][num_cols - 1]:
                return search_row(matrix[row], target)
            elif target < matrix[row][0]:
                end = row
            else:
                start = row + 1
        
        return False

    
def search_row(row: List[int], target: int) -> bool:
    start = 0
    end = len(row)
    while start < end:
        idx = start + ((end - start) // 2)
        if row[idx] == target:
            return True
        elif row[idx] > target:
            end = idx
        else:
            start = idx + 1
    return False
