from typing import List

"""
This is when the matrix is not sorted globally else it is sorted by rows and columns.
So, we can not use the  1-d binary search logic.
"""

"""
The logic here is to use row and col same as binary serach. We start from top right corner
because that corner row and column becomes like 1 d sorted array and we compare the current element with the
target if its greater than target then it means it lies left of the current so we eleminate the current column
by decrementing by one and if target is greater then it means that it does not lie in current row and we
increment the current row by one.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = 0, len(matrix[0]) -1

        while row < len(matrix) and col >= 0:
            curr_ele = matrix[row][col]
            if curr_ele == target:
                return True
            elif curr_ele > target:
                col -= 1
            else:
                row += 1
        
        return False