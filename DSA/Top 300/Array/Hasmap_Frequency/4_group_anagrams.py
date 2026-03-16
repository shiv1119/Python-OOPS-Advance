from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """
        Brute Force - Two strings are anagrams if their sorted values are equals.
        We will use a dictionaly to map the sorted strings - List of anagrams.

        Time - O(N * KlogK) - N Strings, sorting each strings of length K
        Space - O(N*K) -> Storing grouped strings in hashmap
        """
        
        """
        groups = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
        return list(groups.values())

        """
        """
        Optimal - Sorth=ing takes O(KlogK) we can reduce it to you know O(K)
        Using frequency count of characters as key(tuple) if we use dictionary as key then it will work for unicode as well. But uisng tuple it will be very fast for lowercase letter a - z
        """
        # General versions works for any thing
                # Time: O(n * klogk) → faster than sorting for long strings
        #Space: O(n * k) → storing groups and keys

        """groups = defaultdict(list)
        for s in strs:
            freq = {}
            for ch in s:
                freq[ch] = freq.get(ch, 0) + 1
            key = tuple(sorted(freq.items()))
            groups[key].append(s)
        
        return list(groups.values())"""

        # best for a-z only
        # Time: O(n * k) → faster than sorting for long strings
        #Space: O(n * k) → storing groups and keys
        groups = defaultdict(list)
        for s in strs:
            count = [0]*26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            
            key = tuple(count)
            groups[key].append(s)

        return list(groups.values())

        