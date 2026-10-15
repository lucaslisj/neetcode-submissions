class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for index, center in enumerate(s):
            cur = center

            # check for odd palindromes
            dist = 1
            while index - dist >= 0 and index + dist < len(s) and s[index - dist] == s[index + dist]:
                cur = s[index - dist] + cur + s[index + dist]
                dist += 1
            if len(cur) > len(ans):
                ans = cur
                
            
            # check for even palindromes
            if index < len(s) - 1 and center == s[index + 1]:
                dist = 1
                cur = 2 * center 
                while index - dist >= 0 and index + 1 + dist < len(s) and s[index - dist] == s[index + 1 + dist]:
                    cur = s[index - dist] + cur + s[index + 1 + dist]
                    dist += 1
                if len(cur) > len(ans):
                    ans = cur
        return ans

            



        