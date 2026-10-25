class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opn = ['(','[','{']
        for element in s:
            if element in opn:
                stack.append(element)
            elif element == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif element == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            else:
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
        if not stack:
            return True
        return False
                  