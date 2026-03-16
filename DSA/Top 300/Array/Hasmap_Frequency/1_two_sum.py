from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force - Using two loops we can doi this.
        Time - O(N^2), Space - O(N)
        """
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        """

        """
        Better Solution - Hashmap with two pass - 
        1st Pass - Pass all the elements inedx into the hashmap as value and elements as key.
        2nd Pass - Then find out the complements and then check if it exists inside the map if yes then return the index value of it.
        Time - O(N), Space - O(N)
        """
        """
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in h and h[complement] != i:
                return [i, h[complement]]
        """

        """
        Optimal Solution - Using Hashmap with only one pass.
        The idea is to calculate complement and check inside the map if the complement is found then we return the answer.
        """
        h = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in h:
                return [h[complement], i]
            
            h[num] = i 