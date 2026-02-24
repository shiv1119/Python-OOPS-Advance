# Lc - 154. Find Minimum in Rotated Sorted Array II - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:

        """
        Optimal - The idea is to just use binary serach to solve it. find out the unsorted part if we get it then it means the 
        smallest number exists in that - Case if duplicates was not there.
        But if duplicate is there then we need to dhrink the high by -1.
        To reduce the no of operations check if nums low is smaller than nums high if so then it means the array is sorted and return nums[low].

        Time - O(log(N)), Space - O(1)
        """
        low, high = 0, len(nums)-1

        while low < high:

            if nums[low] < nums[high]:
                return nums[low]
            
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high -= 1
        
        return nums[low]
            