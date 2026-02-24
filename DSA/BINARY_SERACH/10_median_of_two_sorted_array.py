# LC - 4. Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/description/

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Brute force - The idea here is to combine the both array using merge short conept and then find out the median of the array.
        Odd - (n // 2)th term will be the median.
        Even - (((n//2)th term + ((n//2) + 1)th term) // 2) will give the median of the two sorted array.
        Time - O(M + N), Space - O(M + N)
        """
        """
        i,j = 0, 0
        m = len(nums1)
        n = len(nums2)
        nums = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        while i < m:
            nums.append(nums1[i])
            i += 1
        while j < n:
            nums.append(nums2[j])
            j += 1
        total = m + n
        if total % 2 == 0:
            mid = total // 2
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            return nums[total // 2]

        """
        """
        Better approach - The idea here is to get the indexes that we need for the median suppose that we have 9 elements combined total then we need 9 // 2 = 4th element onlyt right.
        For even, suppose the length is 8 then second element that we need is the 4th element and the first element will be 4 - 1 element right.
        By doing this we can you know save the spaces.
        Time - O(M+N), Space - O(1)
        """

        """
        count = 0
        i,j = 0, 0
        m = len(nums1)
        n = len(nums2)
        second_idx = (m+n) // 2
        first_idx = second_idx - 1
        first_element = -1
        second_element = -1
        terminated = False

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                if count == first_idx: 
                    first_element = nums1[i]
                if count == second_idx:
                    second_element = nums1[i]
                    terminated = True
                    break
                count += 1
                i += 1
            else:
                if count == first_idx: 
                    first_element = nums2[j]
                if count == second_idx:
                    second_element = nums2[j]
                    terminated = True
                    break
                count += 1
                j += 1
        
        if not terminated:
            while i < m:
                if count == first_idx: 
                    first_element = nums1[i]
                if count == second_idx:
                    second_element = nums1[i]
                    terminated = True
                    break
                count += 1
                i += 1
        
        if not terminated:
            while j < n:
                if count == first_idx: 
                    first_element = nums2[j]
                if count == second_idx:
                    second_element = nums2[j]
                    terminated = True
                    break
                count += 1
                j += 1
        
        if (m+n) % 2 != 0:
            return second_element
        
        return (first_element + second_element) / 2

        """

        """
        Optimal way - The idea is to use binary search to find out the symmetry on which we will get the. The core idea is to partition the array such that 
        Left half total elements = Right half total elements and max(left) <= min(right)
        Time - O(log(M + N)), Space - O(1)

        cut1 = elements taken from nums1 (left side)
        cut2 = elements taken from nums2 (left side)
        cut1 + cut2 = total_left = (m+n+1)//2
        cut2 = total_left - cut1

        we care aboyut these 4 values - 
        l1 = nums1[cut1-1]
        r1 = nums1[cut1]

        l2 = nums2[cut2-1]
        r2 = nums2[cut2]

        we found correct if 
        l1 <= r2 and l2 <= r1
        """

        # Here we want to ensure that the first one is the smallest array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 

        m, n = len(nums1), len(nums2)
        total = m + n 
        half = (total + 1) // 2

        low, high = 0, m

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = half - cut1

            l1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            l2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]

            r1 = float("inf") if cut1 == m else nums1[cut1]
            r2 = float("inf") if cut2 == n else nums2[cut2]

            # if below conditions satisfy then we found correct partition
            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
