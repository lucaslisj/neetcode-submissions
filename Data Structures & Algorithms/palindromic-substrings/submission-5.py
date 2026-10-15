class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for index in range(len(s)):


            # odd palindromes
            l = index
            r = index
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
                



            # even palindromes
            l = index
            r = index + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
        
        return count