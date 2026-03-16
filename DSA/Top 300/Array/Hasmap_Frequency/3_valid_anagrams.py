class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Brute Force - Using sorting technique.
        Time - O(NlogN), Space - O(N)
        """
        # return sorted(s) == sorted(t)

        """
        Optimal - Using hasmap or counter. We cound the frequency in one pass from one string and then in second pass we decrease the count if the element frequency is 0 or not found then it means that is not the anagram and we return false.
        Time - O(N), Space - O(N) (O(26) if all the letters are small case else O(N))
        """
        """
        if len(s) != len(t):
            return False
        
        freq = {}
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return False
            freq[ch] -= 1
        
        return True
        """

        """
        Best - Fixed Sized array instead of hashmap
        Time - O(N), Space - O(26) means O(1)
        """
        if len(s) != len(t):
            return False
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in t:
            count[ord(ch) - ord('a')] -= 1
            if count[ord(ch) - ord('a')] < 0:
                return False
        return True

