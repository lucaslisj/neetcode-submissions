class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # dp approach, work backwards
        ans = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, -1, -1): # we start from second to last cuz final is always 0
            j = i + 1 #future day we are comparing to 
            flag = 0
            while j < len(temperatures) and temperatures[i] >= temperatures[j]:
                if ans[j] == 0: #no warmer days than day j, and we also know that i is not colder than j
                #meaning no warmer days for i later
                    flag = 1 #signifies no need to do anything
                    break
                j += ans[j] # get to the warmer day than index j, could be warmer or colder than i, need to check 
            
            if flag == 0 and j < len(temperatures): # the current j value is warmer than i
                ans[i] = j - i
        return ans


