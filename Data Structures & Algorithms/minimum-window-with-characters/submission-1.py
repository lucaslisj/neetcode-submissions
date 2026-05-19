class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_table_t = {}
        freq_table_s = {}

        min_length = 1001
        ans = ""
        def is_subset(t1,t2) -> bool: #check if one is in another
        # O(26) time = O(1) cuz there are at most 26 letters to check
            for key, value in t1.items():
                if key not in t2:
                    return False
                if value > t2[key]:
                    return False
            return True
        
        # initialize frequecy table of t
        for letter in t:
            freq_table_t[letter] = freq_table_t.get(letter,0) + 1
        
        p1 = 0
        for p2 in range(len(s)):
            letter = s[p2]
            # add in the current letter
            freq_table_s[letter] = freq_table_s.get(letter,0) + 1
        
            # move the left pointer until invalid, checking for validity
            while (is_subset(freq_table_t,freq_table_s)):
                if p2 - p1 + 1 < min_length:
                    ans = s[p1 : p2 + 1]
                min_length = min(min_length, p2 - p1 + 1)
                del_let = s[p1]
                if freq_table_s[del_let] == 1:
                    del freq_table_s[del_let]
                else:
                    freq_table_s[del_let] -= 1
                p1 += 1
        return ans
    
                
        

        
        