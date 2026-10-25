class Solution:
    def isPalindrome(self, s: str) -> bool:
        def keep(letter):
            return (ord('A') <= ord(letter)<=ord('Z')) or (ord('a')<=ord(letter)<=ord('z')) or (ord('0')<=ord(letter)<=ord('9'))
        kept = ""
        left = 0
        for letter in s:
            if keep(letter):
                kept += letter
        right = len(kept) - 1
        while left < right:
            if kept[left].lower() != kept[right].lower():
                return False
            left += 1
            right -= 1
        return True
        