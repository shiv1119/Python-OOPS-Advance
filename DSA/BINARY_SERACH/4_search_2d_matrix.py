from typing import List
"""
We carefull while solving these type of the question beacuse in this the matrix is globally sorted,
but we can get the matrix that is row wise sorted or column wise sorted but not globally.
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0]) 
        low, high = 0, n*m - 1

        while low <= high:
            mid = (low+high) // 2
            mid_ele = matrix[mid // m][mid % m]
            if mid_ele == target:
                return True
            elif mid_ele > target:
                high = mid - 1
            else:
                low = mid + 1
        
        return False
    
#Time - O(log(n*m)), Space - O(1)