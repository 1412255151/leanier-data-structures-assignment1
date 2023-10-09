class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0


def evaluate_postfix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])
    
    for char in expression:
        if char not in operators:
            
            stack.push(int(char))
        else:
            
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            elif char == '/':
                stack.push(operand1 / operand2) 
            
   
    return stack.pop()


postfix_expression = input("Enter a postfix expression: ")


result = evaluate_postfix(postfix_expression)

print("Result:", result)