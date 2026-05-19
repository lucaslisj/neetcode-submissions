class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p1 = 0
        freq_table_s1 = {}
        freq_table_s2 = {}
        for letter in s1:
            if letter in freq_table_s1:
                freq_table_s1[letter] += 1
            else:
                freq_table_s1[letter] = 1
        p2 = 0
        while(p2 < len(s1) - 1):
            letter = s2[p2]
            if letter in freq_table_s2:
                freq_table_s2[letter] += 1
            else:
                freq_table_s2[letter] = 1
            p2 += 1
        while(p2 < len(s2)):
            letter = s2[p2] 
            if letter in freq_table_s2:
                freq_table_s2[letter] += 1
            else:
                freq_table_s2[letter] = 1
            if freq_table_s1 == freq_table_s2:
                return True
            if freq_table_s2[s2[p1]] == 1:
                del freq_table_s2[s2[p1]]
            else:
                freq_table_s2[s2[p1]] -= 1
            p2 += 1
            p1 += 1
        return False
            
        