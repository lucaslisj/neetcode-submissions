class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomletters = {}
        magazineletters = {}
        for letter in magazine:
            if letter in magazineletters:
                magazineletters[letter] += 1
            else:
                magazineletters[letter] = 1
        for letter in ransomNote:
            if letter in ransomletters:
                ransomletters[letter] += 1
            else:
                ransomletters[letter] = 1
        for letter, count in ransomletters.items():
            if letter not in magazineletters:
                return False
            if magazineletters[letter] < count:
                return False
        return True