class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if len(s2) < len(s1):
        #     return False
        freq_table_s1 = {}
        freq_table_s2 = {}

        # initialize freq_table_s1
        for letter in s1:
            freq_table_s1[letter] = freq_table_s1.get(letter,0) + 1

        p1 = 0
        for p2 in range(len(s2)):
            # add the incoming letter
            letter = s2[p2]
            freq_table_s2[letter] = freq_table_s2.get(letter,0) + 1

            # if the window is too long, move the left pointer up until good
            if (p2 - p1 + 1) > len(s1):
                del_let = s2[p1]
                if freq_table_s2[del_let] == 1:
                    del freq_table_s2[del_let]
                else:
                    freq_table_s2[del_let] -= 1
                p1 += 1

            # after moving left pointer up, it might be correct length
            if (p2 - p1 + 1) == len(s1):
                if freq_table_s1 == freq_table_s2:
                    return True
        return False