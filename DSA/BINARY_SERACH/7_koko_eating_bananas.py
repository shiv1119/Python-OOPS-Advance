# LC - 875. Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/description/

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Brutre force - The idea is that the koko can eat min 1 banana and maximun banana that she can eat is
        the max of the piles. So, we loop from 1 to maximum that she can eat and calculate the total hrs that she would take 
        and then return it if that is smaller than or equal to the given hours

        Time - O(Max(piles) * N)
        """

        """
        def calculate_time(piles, i):
            total_time = 0
            for bananas in piles:
                total_time += math.ceil(bananas/i)
            return total_time
        for i in range(1, max(piles)+1):
            if calculate_time(piles, i) <= h:
                return i
        """


        """
        The idea is the we know the min and max that koko can eat and the range will be in sorted order so, we can apply bs to reduce the time complexity to Max(piles) to log(Max(piles))
        Time - O(log(Max(piles)) * N)
        """
        def calculate_time(piles, i):
            total_time = 0
            for bananas in piles:
                total_time += math.ceil(bananas/i)
            return total_time

        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) // 2

            if calculate_time(piles, mid) <= h:
                high = mid
            else:
                low  = mid + 1
        
        return low



