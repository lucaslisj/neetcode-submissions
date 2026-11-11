class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        curlets = set()
        ans = 0
        while r < len(s):
            if s[r] in curlets:
                while s[r] in curlets:
                    curlets.remove(s[l])
                    l += 1
            curlets.add(s[r])
            ans = max(r - l + 1, ans)
            r += 1

        return ans
