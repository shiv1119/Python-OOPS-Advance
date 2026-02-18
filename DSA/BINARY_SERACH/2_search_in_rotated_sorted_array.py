#LC - 33 - https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            # Check which side is sorted if nums low is smaller than the nums mid then the left side is sorted and we search in that        
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            
            else:
                # It means that right side is sorted and we search in that for target
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1



