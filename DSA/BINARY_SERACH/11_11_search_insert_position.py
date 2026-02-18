# 35. Search Insert Position - https://leetcode.com/problems/search-insert-position/description/

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        low, high = 0, len(nums)-1

        while low <= high:
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        
        return low