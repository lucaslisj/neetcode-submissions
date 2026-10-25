class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        seentwice = set()
        for letter in s:
            if letter not in seen:
                seen.add(letter)
            elif letter in seen:
                seentwice.add(letter)

        for index, letter in enumerate(s):
            if letter not in seentwice:
                return index
        
        return -1