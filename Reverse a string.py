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


input_string = input("Enter a string: ")


stack = Stack()


for char in input_string:
    stack.push(char)


reversed_string = ""
while not stack.is_empty():
    reversed_string += stack.pop()

print("Reversed string:", reversed_string)