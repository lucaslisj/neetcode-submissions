class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = ['[]','{}','()']
        for letter in s:
            if letter == '[' or letter == '{' or letter == '(':
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                p = stack.pop()
                if p + letter not in valid:
                    return False
        return len(stack) == 0 
        