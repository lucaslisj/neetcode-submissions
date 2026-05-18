class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        let1 = {}
        let2 = {}
        for letter in s:
            if letter in let1:
                let1[letter] += 1
            else:
                let1[letter] = 1
        for letter in t:
            if letter in let2:
                let2[letter] += 1
            else:
                let2[letter] = 1
        return let1 == let2
