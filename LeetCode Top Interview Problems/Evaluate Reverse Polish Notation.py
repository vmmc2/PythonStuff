class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for element in tokens:
            if element != "+" and element != "-" and element != "*" and element != "/": # peguei um numero...
                stack.append(int(element))
            else: #peguei um operador...
                if element == "+":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 + num2)
                elif element == "-":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 - num2)
                elif element == "*":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(num1 * num2)
                elif element == "/":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    if (num1 >= 0 and num2 >= 0) or (num1 < 0 and num2 < 0):
                        stack.append(num1//num2)
                    else:
                        num1 = abs(num1)
                        num2 = abs(num2)
                        v = num1//num2
                        stack.append((-1)*v)
        return stack[-1]
