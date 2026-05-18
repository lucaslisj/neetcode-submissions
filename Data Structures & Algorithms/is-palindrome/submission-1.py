class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = "".join(c.lower() for c in s if (c.isalpha() or c.isdigit()))
        i = 0
        j = len(txt) - 1
        while(i < j):
            if txt[i] != txt[j]:
                return False
            i += 1
            j -= 1
        return True
