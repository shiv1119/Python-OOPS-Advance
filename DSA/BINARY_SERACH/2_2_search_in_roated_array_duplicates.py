#Lc - 81 - https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
from typing import List

"""
Search in Rotated Array with Duplicates - Similar to LC - 33 just we need to do extra check for
same elements through out the list. If there are same elements then  binary serach will not work
we need to just shrink the range by 1. 
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums)-1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] == nums[high]:
                high -= 1
                low += 1
            elif nums[low] <=nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high  = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

# Time - O(N) worst, Space O(N)