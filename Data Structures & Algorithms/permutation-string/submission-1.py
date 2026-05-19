class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        freq_table_s1 = {}
        freq_table_s2 = {}

        # initialize freq_table_s1
        for letter in s1:
            freq_table_s1[letter] = freq_table_s1.get(letter,0) + 1
        
        # start iterating
        p1 = 0
        for p2 in range(len(s2)):
            letter = s2[p2]
            # our window is from p1 to p2
            # the window could be too short for the first len(s1) iterations

            #1. add the p2 letter to our current hashtable

            freq_table_s2[letter] = freq_table_s2.get(letter,0) + 1

            #2. check window length (too short)
            if (p2 - p1 + 1 < len(s1)):
                continue

            #3. means that our window is perfect length
            elif (p2 - p1 + 1 == len(s1)):
                if freq_table_s2 == freq_table_s1:
                    return True
                del_let = s2[p1]
                if freq_table_s2[del_let] == 1:
                    del freq_table_s2[del_let]
                else:
                    freq_table_s2[del_let] -= 1
                p1 += 1
        return False