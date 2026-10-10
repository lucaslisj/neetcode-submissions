class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
        for letter in s:
            dict1[letter] = dict1.get(letter,0) + 1
        for letter in t:
            dict2[letter] = dict2.get(letter,0) + 1
        return dict1 == dict2
        