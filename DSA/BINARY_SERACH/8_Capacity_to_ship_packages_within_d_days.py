# LC - 1011. Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        """
        Brute force - What we can do is that we can get the max of the weights and sum of the weights that will be our range. 
        So, we can loop and findout the total days that will take to ship the weights and if its smaller that or equal to days then return it.

        Time - O((sum(weights) - max(weights)) * N) or O(sum(weights) * N), Space - O(N)
        """
        """
        def calculate_days(weights, cap):
            net_days = 1
            curr_load = 0
            for wt in weights:
                if curr_load + wt > cap:
                    net_days += 1
                    curr_load = 0
                curr_load += wt
            return net_days

        for i in range(max(weights), sum(weights)+1):
            if calculate_days(weights, i) <= days:
                return i

        """

        """
        Optimal - Binary Search On Answers - In this we get the range as max(weights) to sum(weights). Apply BS and you are good to go.
        Time - O(log(sum(weights)) * N)
        """

        def calculate_days(weights, cap):
            net_days = 1
            curr_load = 0
            for wt in weights:
                if curr_load + wt > cap:
                    net_days += 1
                    curr_load = 0
                curr_load += wt
            return net_days
        
        low, high = max(weights), sum(weights)

        while low < high:
            mid = (low + high) // 2
            if calculate_days(weights, mid) <= days:
                high = mid
            else:
                low = mid + 1
        return low


        