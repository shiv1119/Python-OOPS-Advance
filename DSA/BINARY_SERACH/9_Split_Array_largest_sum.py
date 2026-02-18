# LC - 410. Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/description/

from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
        Brute force - Get the range which will be max(nums) to sum(nums) and then get the sum of the subarrays and check if that is smaller than or equal to the given k if so return the sum of the subarray passing the condition.
        Time - O(sum(nums) * N)
        """
        """
        def get_split_sum_coun(nums, max_sum):
            count = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > max_sum:
                    count += 1
                    curr_sum = 0
                curr_sum += num
            return count

        for i in range(max(nums), sum(nums) + 1):
            if get_split_sum_coun(nums, i) <= k:
                return i

        """

        """
        Optimal - Binary Search on Answers - As we can clearliy see the ranges from max(nums) to sum(nums) we can apply binary search over here right.
        Time - O(log(sum(nums)) * N)
        """

        def get_split_sum_count(nums, max_sum):
            count = 1
            curr_sum = 0
            for num in nums:
                if num + curr_sum > max_sum:
                    count += 1
                    curr_sum = 0
                curr_sum += num 
            
            return count
        
        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            if get_split_sum_count(nums, mid) <= k:
                high = mid
            else:
                low = mid + 1
        
        return low