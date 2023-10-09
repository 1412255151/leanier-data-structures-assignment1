class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
    
    def reverse(self, head, k):
        prev = None
        current = head
        next = None
        count = 0
        
        
        temp = head
        while temp and count < k:
            temp = temp.next
            count += 1
        
        
        if count == k:
            while current and count > 0:
                next = current.next
                current.next = prev
                prev = current
                current = next
                count -= 1
            
            
            if next:
                head.next = self.reverse(next, k)
        
        return prev
    
    def reverse_in_groups(self, k):
        self.head = self.reverse(self.head, k)
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


values = list(map(int, input("Enter space-separated values for the linked list: ").split()))
k = int(input("Enter the group size: "))


ll = LinkedList()
for value in values:
    ll.insert(value)

print("Original Linked List:")
ll.display()

ll.reverse_in_groups(k)

print(f"Linked List after reversing in groups of {k}:")
ll.display()