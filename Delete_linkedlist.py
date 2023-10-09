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

    def delete_zero_sum_sublists(self):
        cumulative_sum = 0
        sum_dict = {}
        temp = self.head
        while temp:
            cumulative_sum += temp.data
            if cumulative_sum == 0:

                self.head = temp.next
                sum_dict.clear()
            elif cumulative_sum in sum_dict:

                sum_node = sum_dict[cumulative_sum]
                sum_node.next = temp.next
            else:
                sum_dict[cumulative_sum] = temp
            temp = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


values = list(map(int, input("Enter space-separated values for the linked list: ").split()))


ll = LinkedList()
for value in values:
    ll.insert(value)

print("Original Linked List:")
ll.display()

ll.delete_zero_sum_sublists()

print("Linked List after deleting zero sum sublists:")
ll.display()