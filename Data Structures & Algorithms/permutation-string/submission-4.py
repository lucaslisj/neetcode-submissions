class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1counts = {}
        for letter in s1:
            if letter in s1counts:
                s1counts[letter] += 1
            else:
                s1counts[letter] = 1
        curcounts = {}
        l = 0
        for r in range(len(s2)):
            letter = s2[r]
            curcounts[letter] = curcounts.get(letter,0) + 1

            if(r - l + 1) > len(s1):
                let = s2[l]
                if curcounts[let] == 1:
                    del curcounts[let]
                else:
                    curcounts[let] -= 1
                l += 1
            
            if (r - l + 1) == len(s1):
                if curcounts == s1counts:
                    return True
        return False
