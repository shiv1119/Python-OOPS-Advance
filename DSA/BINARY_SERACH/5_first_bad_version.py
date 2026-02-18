# Lc- 278. First Bad Version - https://leetcode.com/problems/first-bad-version/description/
from typing import List

"""
Hell this one is confusing. So in this what we have to do we have to find ou the first 
bad version of the product beacuse after that all will be bad.
"""


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n

        while low < high:
            mid = (low+high)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        
        return low