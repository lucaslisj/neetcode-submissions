class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        scounts = {}
        tcounts = {}
        for letter in s:
            if letter in scounts:
                scounts[letter] += 1
            else:
                scounts[letter] = 1
        for letter in t:
            if letter in tcounts:
                tcounts[letter] += 1
            else:
                tcounts[letter] = 1
        return scounts == tcounts
