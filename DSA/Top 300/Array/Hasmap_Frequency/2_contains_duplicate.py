from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Brute Force - Use two loops and if the elements equals then we have duplicate.
        Time - O(N^2), Space - O(1)
        """
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False 
        """

        """
        Optimal - Use hasmap or set. We will use set as seen if the number is already present inside the set seen then it means conatins duplicate.
        Time - O(N), Space - O(N) 
        """

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False