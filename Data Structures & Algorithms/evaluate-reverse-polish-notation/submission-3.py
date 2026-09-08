class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # basically the logic is while iterating through the tokens 
        # if you find + and * then we just append those operations done in and add 
        # add it to the stack
        # Else we have two variables a,b and do the required operations 

        stack = []

        for char in tokens:
            if char =='+':
                stack.append(stack.pop()+ stack.pop())
            elif char == '-':
                a,b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif char == '*':
                stack.append(stack.pop()*stack.pop())
            elif char == '/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(char))
        

        return stack[0]