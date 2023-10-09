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

    def merge_alternate(self, other_list):
        current_self = self.head
        current_other = other_list.head


        while current_self is not None and current_other is not None:

            next_self = current_self.next
            next_other = current_other.next


            current_self.next = current_other
            current_other.next = next_self


            current_self = next_self
            current_other = next_other


        other_list.head = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


values1 = list(map(int, input("Enter space-separated values for the first linked list: ").split()))
ll1 = LinkedList()
for value in values1:
    ll1.insert(value)


values2 = list(map(int, input("Enter space-separated values for the second linked list: ").split()))
ll2 = LinkedList()
for value in values2:
    ll2.insert(value)


ll1.merge_alternate(ll2)

print("Linked List after merging at alternate positions:")
ll1.display()