class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        p1 = 0
        ans = 0
        freq_table: dict[str,int] = {}

        def getmax(table: dict[str,int]) -> int:
            ans = 0
            for key, value in table.items():
                ans = max(ans, value)
            return ans

        for p2 in range(len(s)):
            #update the current letter into it
            cur = s[p2]
            if cur not in freq_table:
                freq_table[cur] = 1
            else:
                freq_table[cur] += 1
            
            #check if the string from s[p1] to s[p2] (both inclusive) inclusive is valid

            maxx = getmax(freq_table)
            
            while (p2 - p1 + 1 - maxx > k): ## not valid
                freq_table[s[p1]] -= 1
                p1 += 1
                maxx = getmax(freq_table)
            
            ans = max(ans, p2 - p1 + 1)
        return ans
            




        
            

