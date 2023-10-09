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


class QueueUsingStacks:
    def __init__(self):
        self.stack1 = Stack() 
        self.stack2 = Stack() 
    
    def enqueue(self, item):
        self.stack1.push(item)
    
    def dequeue(self):
        if self.stack2.is_empty():
            
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()


queue = QueueUsingStacks()


while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = int(input("Enter the element to enqueue: "))
        queue.enqueue(item)
    elif choice == 2:
        dequeued_item = queue.dequeue()
        if dequeued_item is not None:
            print("Dequeued element:", dequeued_item)
        else:
            print("Queue is empty.")
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")