class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','*','/'}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                if token == '-':
                    stack.append(num2 - num1)
                if token == '*':
                    stack.append(num1 * num2)
                if token == '/':
                    stack.append(int(num2 / num1))
            for element in stack:
                print(element)
            print()
        return stack[0]
