class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1) # of ways to decode length n string for this current formulation
        if s[0] == "0":
            return 0
        dp[0] = 1
        dp[1] = 1
        combine = {"12","13","14","15","16","17","18","19","11","21","22","23","24","25","26"}
        for i in range(2, len(s) + 1):
            zeroindex = i - 1
            cur = s[zeroindex]
            if cur == "0":
                if s[zeroindex - 1] != "1" and s[zeroindex - 1] != "2":
                    return 0
                dp[i] = dp[i - 2]
            elif s[zeroindex - 1: zeroindex + 1] in combine:
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[len(s)]



        