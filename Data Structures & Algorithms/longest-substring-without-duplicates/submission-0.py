class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current = set() #elements
        ans = 0
        p1 = 0
        p2 = 0
        while (p2 < len(s)):
            if s[p2] not in current:
                current.add(s[p2])
                p2 += 1
                ans = max(p2-p1,ans)
            else:
                while s[p2] in current:
                    current.remove(s[p1])
                    p1 += 1
        return ans
