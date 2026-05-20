class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index_stack = [] #contains a monotonically decreasing stack, if any number is larger than the top, keep popping and append till the end
        # we manually compute values based on stored indices and any indices left over have no larger temps later on
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            cur_temp = temperatures[i]

            # add into the stack if empty
            if len(index_stack) == 0:
                index_stack.append(i)
            
            #keep checking and updating 
            else:
                # remove all the previous days that are less than this temperature
                while len(index_stack) > 0 and temperatures[index_stack[-1]] < cur_temp:
                    ok_index = index_stack.pop()
                    ans[ok_index] = i - ok_index 
                
                # add current temp to the stack (index of it)
                index_stack.append(i)
        return ans
