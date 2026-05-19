class MinStack:
    
    def __init__(self):
        self.stk = [] # tracks literal elements
        self.min_stk = [] # tracks the index of the smallest element

    def push(self, val: int) -> None:
        self.stk.append(val)
        index_of_min = 0
        if len(self.stk) == 1:
            pass
        else:
            prev_index_of_min = self.min_stk[-1]
            prev_min = self.stk[prev_index_of_min]
            if val < prev_min:
                index_of_min = len(self.stk) - 1
            else:
                index_of_min = prev_index_of_min
        self.min_stk.append(index_of_min)



    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.stk[self.min_stk[-1]]
        
