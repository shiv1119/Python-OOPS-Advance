from typing import List

"""
In this question we try to find out the first occurance and then last occurance. We need to be
very carful while finding out the last occurance while determining the mid value beacuse if we do noraml wise then it can lead to 
oinfinite loop or time limit exceeds.
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high) // 2

            if nums[mid] >= target:
                high = mid
            else:
                low  = mid + 1

        if nums[low] != target:
            return [-1, -1]
        first = low

        low, high = 0, len(nums) - 1
        while low < high:
            mid = low + (high - low + 1) // 2
            if nums[mid] <= target:
                low = mid
            else:
                high = mid - 1
        last = low

        return [first, last]
                    