class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        seventonine = {"7","8","9"}
        onetwo = {"1","2"}
        threetosix = {"3","4","5","6"}
        if s[0] == "0":
            return 0
        dp[0] = 1 # we write like this so that we can always go back two prev. so that in cases where the 2nd letter can attach we add 1 extra possbility
        dp[1] = 1 #first letter has 1 possibility

        for index in range(2,len(s) + 1): #index represents the letter count, ie index = 2 means we on the second letter
            zeroindex = index - 1
            cur = s[zeroindex]
            if cur == "0":
                if s[zeroindex - 1] not in onetwo: # no valid
                    return 0
                dp[index] = dp[index - 1] # has to be attached to the previous one
            elif cur in onetwo:
                if zeroindex + 1 < len(s) and s[zeroindex + 1] == "0": #next is 0, have to attach with next
                    dp[index] = dp[index - 1]
                elif s[zeroindex - 1] in onetwo: #next isn't 0, we can combine with prev or just simply add on
                    dp[index] = dp[index - 1] + dp[index - 2]
                else: # next isn't 0, but we can't combine with the previous one
                    dp[index] = dp[index - 1]
            elif cur in threetosix:
                if s[zeroindex - 1] in onetwo: #can attach
                    dp[index] = dp[index - 1] + dp[index - 2]
                else:
                    dp[index] = dp[index - 1]
            else: #seven to nine
                if s[zeroindex - 1] == "1":
                    dp[index] = dp[index - 1] + dp[index - 2]
                else:
                    dp[index] = dp[index - 1]
        return dp[len(s)]
           