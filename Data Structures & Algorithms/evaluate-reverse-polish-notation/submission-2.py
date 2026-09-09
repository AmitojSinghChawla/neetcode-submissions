class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens :

            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a,b = stack.pop(), stack.pop()
                result = b - a
                stack.append(result)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                a, b = stack.pop(), stack.pop()
                result = (int(float(b/a)))
                stack.append(result)
            else:
                stack.append(int(i))

        return stack[0]
                


        