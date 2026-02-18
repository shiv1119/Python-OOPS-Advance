from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # The core logic is to check where unsorted part exists - 
        # Compare nums[mid] > nums[high] then min is in right part 
        # else its in left part including mid


        low, high = 0, len(nums)-1

        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid 

        return nums[low]